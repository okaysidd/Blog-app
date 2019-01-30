from django.urls import path
from .views import CreatePostView, ListPostView, DetailPostView, UpdatePostView, DeletePostView


app_name = "blogs"

urlpatterns = [
    path('new-post/', CreatePostView.as_view(), name="new-post"),
    path('', ListPostView.as_view(), name="all-post"),
    path('post/<int:pk>/', DetailPostView.as_view(), name="post"),
    path('post/<int:pk>/edit', UpdatePostView.as_view(), name="edit-post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete-post"),
]
