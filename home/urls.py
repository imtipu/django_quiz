from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path('', HomeIndex.as_view(), name='home_index')
]