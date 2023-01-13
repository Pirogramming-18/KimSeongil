from django.urls import include, path
from server.apps.review.views import review_list, review_detail, review_create, review_delete, review_update

urlpatterns = [
    path("", review_list, name='review_list'),
    path("review/create", review_create),
    path("review/<int:pk>", review_detail),
    path("review/<int:pk>/delete", review_delete),
    path("review/<int:pk>/update", review_update),
]
