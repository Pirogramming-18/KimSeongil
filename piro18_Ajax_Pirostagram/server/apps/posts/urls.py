from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.posts_list, name='list'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('comment_ajax/', views.comment_ajax, name='comment_ajax'),
    path('comment_delete_ajax/', views.comment_delete_ajax, name='comment_delete_ajax'),
]
