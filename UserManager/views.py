from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import FormView
from django.urls import reverse_lazy

from .models import User

# Create your views here.

def login(request):
    return render(request, 'UserManager/login.html')

class UserRegister(FormView):
    model = User
    form_class = UserCreationForm
    template_name = 'UserManager/register.html'
    success_url = reverse_lazy('marathon_home')

def profile(request):
    return render(request, 'UserManager/profile.html')
