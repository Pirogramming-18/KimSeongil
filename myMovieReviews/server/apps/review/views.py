from django.shortcuts import render, redirect
from server.apps.review.models import review


def review_list(request, *args, **kwargs):
    reviews = review.objects.all()

    sort_by = request.GET.get('sort', 'seq')
    if sort_by == 'seq':
        reviews = review.objects.all().order_by("id")
    elif sort_by == 'title':
        reviews = review.objects.all().order_by("title")
    elif sort_by == 'stats':
        reviews = review.objects.all().order_by("-stats")
    elif sort_by == 'running_time':
        reviews = review.objects.all().order_by("-running_time")
    elif sort_by == 'release_year':
        reviews = review.objects.all().order_by("-release_year", "-stats")
    print(sort_by)
    return render(request, "review/review_list.html", {"reviews": reviews, "sort_by": sort_by})


def review_detail(request, pk, *args, **kwargs):
    rv = review.objects.all().get(pk=pk)
    rt = int(rv.running_time)
    rv.running_time = str(rt // 60) + '시간 ' + str(rt % 60) + '분'
    # DO NOT SAVE object!!
    return render(request, "review/review_detail.html", {"review": rv})


def review_create(request, *args, **kwargs):
    if request.method == "POST":
        review.objects.create(
            title=request.POST["title"],
            release_year=request.POST["release_year"],
            genre=request.POST["genre"],
            stats=request.POST["stats"],
            running_time=request.POST["running_time"],
            content=request.POST["content"],
            director=request.POST["director"],
            lead_actor=request.POST["lead_actor"],
        )
        return redirect("/")
    return render(request, "review/review_create.html")


def review_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        rv = review.objects.get(pk=pk)
        rv.delete()
    return redirect("/")


def review_update(request, pk, *args, **kwargs):
    rv = review.objects.get(pk=pk)
    if request.method == "POST":
        rv.title = request.POST["title"]
        rv.release_year = request.POST["release_year"]
        rv.genre = request.POST["genre"]
        rv.stats = request.POST["stats"]
        rv.running_time = request.POST["running_time"]
        rv.content = request.POST["content"]
        rv.director = request.POST["director"]
        rv.lead_actor = request.POST["lead_actor"]
        rv.save()
        return redirect(f"/review/{pk}")
    return render(request, "review/review_update.html", {"review": rv})
