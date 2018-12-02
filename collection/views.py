from django.shortcuts import render, redirect
from collection.forms import PostForm
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib.auth.views import login_required
# from django.http import Http404
from collection.models import Post
from django.db.models import Count, Q
from django.template.defaultfilters import slugify


# grabs objects and passes to the template


def index(request):
    posts = Post.objects.all().annotate(
        num_of_votes=Count('votes'),
        vote_of_user=Count(
            'votes',
            filter=Q(votes__user=request.user))).order_by('-num_of_votes')
    return render(request, 'index.html', {
        'posts': posts
    })


def post_detail(request, slug):
    post = Post.object.get(slug=slug)
    return render(request, 'posts/post_detail.html', {
        'post': post,
    })


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publication_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {
        'form': form
    })


@login_required
def toggle_vote(request):
    pass

    # def render_post_list(request, header, posts):
    #     """want this to render if user is authenticated with title, link, description """
    # posts = posts.annotate(num_of_favorites=Count('favorites'))
    # favorite_posts = []
    # if request.user.is_authenticated:
    #     favorite_posts = request.user.favorite_posts.all()
    # posts = posts.order_by('-created_at')
    # return render(
    #     request, "collection/index.html", {
    #         "title": title,
    #         "link": link,
    #         "description": description
    #     }
    # )
