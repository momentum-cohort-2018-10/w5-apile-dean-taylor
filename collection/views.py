from django.shortcuts import render
from collection.forms import PostForm
from django.views.decorators.http import require_POST
from django.utils import timezone
# from django.contrib.auth.views import login_required
# from django.http import Http404
from collection.models import Post
# from django.db.models import Count
# from django.template.defaultfilters import slugify


# grabs objects and passes to the template


def index(request):
    posts = Post.objects.all()
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
            return redirect('index.hmtl', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {
        'form': form
    })


# DJANGO GIRLS to be edited from above
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})


# def create_post(request):
#     form = PostForm
#     if request.method == 'POST':
#         form = PostForm
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.slug = slugify(post.name)
#             post.save()
#             return redirect('post_detail', slug=post.slug)
#     else:
#         form = form(instance=post)

#     return render(request, 'posts/create_post.html'), {
#         'form': form,
#     }

# @login_required
# def edit_post(request, slug):
#     post = Post.objects.get(slug=slug)
#     if post.user != request.user:
#         raise Http404
#     form_class = PostForm
#     if request.method == 'POST':
#         form = form_class(data=request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_detail', slug=post.slug)

#     else:
#         form = form_class(instance=post)

#     return render(request, 'posts/edit_post.html', {
#         'post': post,
#         'form': form,
#     })

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
