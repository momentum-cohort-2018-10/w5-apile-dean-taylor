from django.contrib import admin
from collection.models import Post, Vote
# from django.contrib.auth.models import User


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'author', 'text')
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Vote)
