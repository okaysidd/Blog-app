from django.urls import path
from .views import profile, DetailProfileView, updateProfile


app_name = "users"

urlpatterns = [
    path('profile/create/', profile, name="create-profile"),
    path('profile/<int:pk>/', DetailProfileView.as_view(), name="view-profile"),
    path('profile/edit/', updateProfile, name="edit-profile"),
]
