from django.shortcuts import render, redirect, get_object_or_404
from collection.forms import PostForm
from django.views.decorators.http import require_POST
from django.utils import timezone
#from django.contrib.auth.views import login_required
from collection.models import Post, Vote
from django.db.models import Count
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# grabs objects and passes to the template


def index(request):
    page = request.GET.get('page', 1)
    sort_pub_date = request.GET.get('sort_pub_date', "desc")
    sort_votes = request.GET.get('sort_votes', "desc")

    order_pub_date = "-published_date"
    if(sort_pub_date == "asc"):
        order_pub_date = "published_date"
    
    order_votes = "-vote_count"
    if(sort_votes == "asc"):
        order_votes = "vote_count"

    postList = Post.objects.all().annotate(
        vote_count=Count('vote')).order_by(order_votes, 
                order_pub_date)
    paginator = Paginator(postList, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {
        'posts': posts,
        'sort_votes': sort_votes,
        'sort_pub_date': sort_pub_date
    })


def post_detail(request, postid):
    post = get_object_or_404(Post, pk=postid)
    vote_count = Vote.objects.filter(post=post).count()
    is_voted = Vote.objects.filter(post=post, author=request.user)
    return render(request, 'posts/post_detail.html', {
        'post': post,
        'is_voted': is_voted,
        'vote_count': vote_count,
    })


def vote_post(request, postid):
    vote = Vote()
    vote.author = request.user
    vote.post = Post.objects.filter(pk=postid)
    vote.save()
    return redirect('post_detail', postid=postid)
    

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', postid=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


def edit_post(request, postid):
    post = get_object_or_404(Post, pk=postid)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', postid=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form})
