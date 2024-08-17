
from django.urls import path

from . import views


urlpatterns = [
    path('login', views.login, name='user_login'),
    path('register', views.UserRegister.as_view(), name='user_register'),
    path('profile', views.profile, name='user_profile'),
]
