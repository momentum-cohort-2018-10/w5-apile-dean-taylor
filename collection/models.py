from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


# New Class
class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    url = models.URLField(unique=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    voted_users = models.ManyToManyField(
        User, through='Vote', related_name='vote_posts')
    # slug = models.SlugField(unique=True, max_length=255, null=True)
    
    def slug(self): return self.pk
    
    def __str__(self):
        return self.title


class Vote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def user(self): return self.author
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def slug(self): return self.pk
    
    def __str__(self):
        return self.author.username + " - " + self.post.title
    
    class Meta:
        unique_together = ("author", "post")
        