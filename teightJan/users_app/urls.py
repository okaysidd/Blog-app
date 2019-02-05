from django.urls import path
from .views import profile, DetailProfileView, updateProfile, profileView, create_social_profile


app_name = "users"

urlpatterns = [
    path('profile/create/', profile, name="create-profile"),
    # path('profile/<int:pk>/', DetailProfileView.as_view(), name="view-profile"),
    path('profile/<int:pk>/', profileView, name="view-profile"),
    path('profile/edit/', updateProfile, name="edit-profile"),
    path('profile/edit/social/', create_social_profile, name="edit-social-profile"),
]
