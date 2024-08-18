
from django.urls import path

from . import views


urlpatterns = [
    # path('login', views.UserLogin.as_view(), name='user_login'),
    # path('register', views.UserRegister.as_view(), name='user_register'),
    path('register', views.register, name='user_register'),
    path('profile', views.profile, name='user_profile'),
]
