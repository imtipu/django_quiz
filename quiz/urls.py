from django.urls import path
from .views import *

app_name = 'quiz'
urlpatterns = [
    path('exams/', ExamList.as_view(), name='exams'),
    path('exams/<int:pk>/questions/', ExamQuestionList.as_view(), name='exam_questions'),
    # path('user-exams/<int:pk>/', UserExamList.as_view(), name='user_exams'),
    # path('user-exams/<int:pk>/', UserExamDetail.as_view(), name='user_exam_detail'),
]
