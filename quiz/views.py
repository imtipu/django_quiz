from django.db.models import Count, Q
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
        return UserExam.objects.filter(user_id=self.kwargs['pk']).order_by('-created')


class UserExamDetail(DetailView):
    template_name = 'quiz/user_exams/detail.html'
    context_object_name = 'user_exam'
    model = UserExam

    # pk_url_kwarg = 'exam_id'
    #
    queryset = UserExam.objects.all()

    def get_object(self, queryset=None):
        # query = UserExam.objects.select_related('user', 'exam').prefetch_related(
        #     'answer_user_exam__answers',
        #     # 'answer_user_exam__answers__questionanswer_set',
        #     'answer_user_exam__question',
        #     'answer_user_exam__question__choice_question',
        # ).annotate(
        #     count_correct_answer=Count('answer_user_exam__question__choice_question',
        #                                filter=
        #                                Q(
        #                                    answer_user_exam__question__choice_question__is_answer=True)
        #                                )).values('count_correct_answer') \
        #     .get(id=self.kwargs['exam_id'])
        # print(query)
        return UserExam.objects.select_related('user', 'exam').prefetch_related(
            'answer_user_exam__answers',
            # 'answer_user_exam__answers__questionanswer_set',
            'answer_user_exam__question',
            'answer_user_exam__question__choices',
            'answer_user_exam__question__correct_choices',
        ).get(id=self.kwargs['exam_id'])
