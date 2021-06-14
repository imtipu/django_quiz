from django.urls import path

from quiz.views import UserExamList, UserExamDetail
from .views import *

app_name = 'users'
urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
    path('<int:pk>/exams/', UserExamList.as_view(), name='user_exams'),
    path('<int:pk>/exams/<int:exam_id>/', UserExamDetail.as_view(), name='user_exam_detail'),
]
