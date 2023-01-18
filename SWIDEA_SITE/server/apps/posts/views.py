from django.shortcuts import render, redirect
from server.apps.posts.models import Tool, Idea, IdeaStar
from django.db.models import Count


def posts_list(request, *args, **kwargs):
    idea = Idea.objects.all()

    if request.method == "POST":
        favorite_pk = request.POST.get('favorite_pk')
        action = request.POST.get('action')
        if favorite_pk and action == 'favorite':
            idea_instance = Idea.objects.get(pk=int(favorite_pk))
            try:
                idea_star = IdeaStar.objects.get(idea=idea_instance)
                idea_star.delete()
            except IdeaStar.DoesNotExist:
                idea_star = IdeaStar.objects.create(idea=idea_instance)
        else:
            pass

    sort_by = request.GET.get('sort')
    if sort_by == 'likes':
        idea = idea.annotate(likes_count=Count(
            'like_idea')).order_by("-likes_count")
    elif sort_by == 'title':
        idea = Idea.objects.all().order_by("title")
    elif sort_by == 'id':
        idea = Idea.objects.all().order_by("id")
    elif sort_by == 'recent':
        idea = Idea.objects.all().order_by("-id")
        print(sort_by)

    if request.method == 'POST':
        form = request.POST
        idea_pk = form.get('idea_pk')
        if idea_pk:
            id = Idea.objects.get(pk=idea_pk)
            if 'minus' in form:
                id.interest -= 1
                id.save()
            elif 'plus' in form:
                id.interest += 1
                id.save()

    context = {
        "ideas": idea,
        "sort_by": sort_by,
    }

    return render(request, "posts/posts_list.html", context=context)


def posts_retrieve(request, pk, *args, **kwargs):
    post = Idea.objects.get(id=pk)
    user = post.user
    all_post = user.post_user.all()

    user_name = post.user.name
    user_age = post.user.age
    context = {
        "post": post,
        "user_name": user_name,
        "user_age": user_age,
        "all_post": all_post,
    }
    return render(request, "posts/posts_retrieve.html", context=context)


def posts_create_idea(request, *args, **kwargs):
    tools = Tool.objects.all()
    if request.method == "POST":
        tool_id = request.POST["devtool"]
        devtool = Tool.objects.get(id=tool_id)
        Idea.objects.create(
            title=request.POST["title"],
            image=request.FILES["image"],
            content=request.POST["content"],
            interest=request.POST["interest"],
            devtool=devtool,
        )
        return redirect("/")
    return render(request, "posts/posts_create_idea.html", {'tools': tools})


def posts_create_tool(request, *args, **kwargs):
    if request.method == "POST":
        Tool.objects.create(
            name=request.POST["name"],
            kind=request.POST["kind"],
            content=request.POST["content"],
        )
        return redirect("/")
    return render(request, "posts/posts_create_tool.html")
