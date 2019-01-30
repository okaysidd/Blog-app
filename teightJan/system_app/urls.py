from django.urls import path
from .views import about, contact, user_login, user_logout


app_name = "system"

urlpatterns = [
    # path('', about, name="about"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),

    # not needed as added LOGIN_URL value in the settings.py file
    # path('accounts/login/', user_login, name="account-login"),
]
