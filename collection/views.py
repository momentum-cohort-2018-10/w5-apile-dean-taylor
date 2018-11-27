from django.shortcuts import render
from collection.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'post': posts
    })
