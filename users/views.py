from django.shortcuts import render
from django.views.generic import *
from .models import *


# Create your views here.
class UserList(ListView):
    template_name = 'users/list.html'
    context_object_name = 'users'
    model = User
