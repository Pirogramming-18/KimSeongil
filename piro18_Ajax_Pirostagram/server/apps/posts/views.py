from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.shortcuts import render, redirect
from server.apps.posts.models import Post, User, Like, Comment
from django.http.request import HttpRequest

# Create your views here.


def posts_list(request: HttpRequest, *args, **kwargs):
    users = User.objects.all()
    posts = Post.objects.all()
    likes = Like.objects.all()
    comments = Comment.objects.all()

    # if request.method == "POST":
    #     like_pk = request.POST.get("like_pk")
    #     action = request.POST.get('like_button')

    #     if like_pk and action == 'like':
    #         post_ins = Post.objects.get(pk=int(like_pk))
    #         try:
    #             like_object = Like.objects.get(post=post_ins)
    #             like_object.delete()
    #         except Like.DoesNotExist:
    #             like_object = Like.objects.create(post=post_ins)
    #     else:
    #         pass

    context = {
        "users": users,
        'posts': posts,
        'likes': likes,
        'comments': comments,
        'like_num': len(likes),
    }
    return render(request, "posts/posts_list.html", context=context)


@csrf_exempt
def like_ajax(request):

    req = json.loads(request.body)

    post_id = req['id']
    post = Post.objects.get(id=post_id)

    whether_like = post.is_favorited()
    if whether_like:
        Like.objects.filter(post=post).delete()
        print("object delete!")
    else:
        Like.objects.create(post=post)
        print("object create!")

    return JsonResponse({'res': 'like', 'id': post_id, 'liked': post.is_favorited()})


@csrf_exempt
def comment_ajax(request):

    req = json.loads(request.body)

    print(req)
    post_id = req['id']
    comment_content = req['value']
    post = Post.objects.get(id=post_id)
    cmt = Comment.objects.create(user="Me", post=post,
                                 content=comment_content)

    return JsonResponse({'res': 'comment', 'id': post_id, 'user_name': "Me", 'content': comment_content, 'cmt_id': cmt.id})


@csrf_exempt
def comment_delete_ajax(request):

    req = json.loads(request.body)
    comment_id = req['id']
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return JsonResponse({'res': 'comment_delete', 'id': comment_id})
