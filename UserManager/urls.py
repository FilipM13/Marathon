
from django.urls import path

from .views import login, register, profile


urlpatterns = [
    path('login', login, name='user_login'),
    path('register', register, name='user_register'),
    path('profile', profile, name='user_profile'),
]
