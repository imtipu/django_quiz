from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import *


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    search_fields = ['username', 'first_name', 'last_name']
