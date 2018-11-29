from django.contrib import admin
from collection.models import Post
from django.contrib.auth.models import User


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('post', 'author', 'text')
    prepopulated_fields = {'slug': ('title',)}



