from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.posts_list, name='list'),
    path("posts/create/idea", views.posts_create_idea, name='create_idea'),
    path("posts/create/tool", views.posts_create_tool, name='create_tool'),
    path("posts/<int:pk>", views.posts_retrieve, name='retrieve'),
    # path("posts/<int:pk>/update", views.posts_update, name='update'),
    # path("posts/<int:pk>/delete", views.posts_delete, name='delete'),
]
