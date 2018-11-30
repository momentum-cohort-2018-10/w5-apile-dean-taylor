from django.db import models
from django.contrib.auth.models import User


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


# New Class
class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    url = models.URLField(unique=True, null=True)
    slug = models.SlugField(unique=True, max_length=255, null=True)

    def __str__(self):
        return self.title



