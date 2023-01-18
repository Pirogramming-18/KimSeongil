from django.shortcuts import render
from server.apps.posts.models import Tool, Idea


def posts_list(request, *args, **kwargs):
    print('posts_list')
    return render(request, "posts/posts_list.html")
