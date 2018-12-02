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
    text = models.TextField(max_length=200)
    url = models.URLField(unique=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=255, null=True)

    def is_voted_by(self, user):
        return self.votes.filter(user=user).count > 0

    def __str__(self):
        return self.title


class Vote(models.Model):
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            'post',
            'user',
        )
