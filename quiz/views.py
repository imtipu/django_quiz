from django.shortcuts import render
from django.views.generic import *
from .models import *


# Create your views here.
class ExamList(ListView):
    template_name = 'quiz/exams/list.html'
    context_object_name = 'exams'
    model = Exam

    def get_queryset(self):
        return Exam.objects.prefetch_related('exam_questions').order_by('title')


class ExamQuestionList(ListView):
    template_name = 'quiz/questions/list.html'
    context_object_name = 'questions'
    model = Question

    def get_queryset(self):
        return Question.objects.prefetch_related('choice_question').filter(exam_id=self.kwargs['pk'])


class UserExamList(ListView):
    template_name = 'quiz/user_exams/list.html'
    context_object_name = 'user_exams'
    model = UserExam

    def get_queryset(self):
        return UserExam.objects.all().order_by('-created')


class UserExamDetail(DetailView):
    template_name = 'quiz/user_exams/detail.html'
    context_object_name = 'user_exam'
    model = UserExam
