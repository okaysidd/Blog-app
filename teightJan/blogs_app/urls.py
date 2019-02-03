from django.urls import path
from .views import CreatePostView, ListPostView, DetailPostView, UpdatePostView, DeletePostView
from .views_comments import createComment


app_name = "blogs"

urlpatterns = [
    path('post/new/', CreatePostView.as_view(), name="new-post"),
    path('', ListPostView.as_view(), name="all-post"),
    path('post/<int:pk>/', DetailPostView.as_view(), name="post"),
    path('post/<int:pk>/edit', UpdatePostView.as_view(), name="edit-post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete-post"),
    path('post/<int:pk>/comment', createComment, name="comment-post"),
]
