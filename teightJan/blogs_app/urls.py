from django.urls import path
from .views import (
                    CreatePostView,
                    ListPostView,
                    DetailPostView,
                    UpdatePostView,
                    DeletePostView,
                    publish_post,
                    DetailPostHistoryView,
                    searchResults,
                    like_post,
                    )
from .views_comments import createComment


app_name = "blogs"

urlpatterns = [
    path('post/new/', CreatePostView.as_view(), name="new-post"),
    # path('post/new/publish', CreatePostView2.as_view(), name="new-publish-post"),
    path('', ListPostView.as_view(), name="all-post"),
    path('post/<int:pk>/', DetailPostView.as_view(), name="post"),
    path('post/<int:pk>/edit', UpdatePostView.as_view(), name="edit-post"),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name="delete-post"),
    path('post/<int:pk>/comment', createComment, name="comment-post"),
    path('post/<int:pk>/publish', publish_post, name="publish-post"),
    path('post/<int:pk>/like', like_post, name="like-post"),
    path('post/<int:pk>/history', DetailPostHistoryView.as_view(), name="history-post"),
    path('search/', searchResults, name="search-results"),
]
