from django.shortcuts import render
from collection.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'post': posts
    })

# grabs objects and passes to the template
def post_detail(request, slug):
    post=Post.objects.get(slug=slug)
    return render(request, 'posts/post_detail.html', {'post': post,
    })