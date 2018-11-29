from django.db import models
from django.contrib.auth.models import User



class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


# New Class
class Post(models.Model):
    post = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=200, default="", editable=False)
    text = models.TextField(max_length=200)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text




# ~~~~~~~~~~~~~~~~~
# class Vote(models.Model):
#     vote = models.BooleanField(null=True)
#     voter = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)