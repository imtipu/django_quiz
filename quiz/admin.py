from django.contrib import admin
from .models import *

from .forms import *
# Register your models here.
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    search_fields = ['title']


@admin.register(UserExam)
class UserExamAdmin(admin.ModelAdmin):
    list_display = ['user', 'exam', 'created']
    search_fields = ['user', 'exam']
    autocomplete_fields = ('user', 'exam')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'question_type', 'created', 'updated']
    search_fields = ['title']


@admin.register(QuestionChoice)
class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'question', 'created', 'updated']
    # prepopulated_fields = {
    #     'question': ('title', )
    # }
    autocomplete_fields = ('question', )


@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ['user_exam', 'question', 'get_question_type', 'get_question_exam', 'check_answer',
                    'created', 'updated']
    readonly_fields = ['check_answer', 'get_question_exam', 'get_question_type']
    autocomplete_fields = ('question', 'user_exam')
    form = QuestionAnswerForm

    def get_question_type(self, instance):
        return '%s' % instance.question.get_question_type_display()

    get_question_type.short_description = 'Type'

    def get_question_exam(self, instance):
        return '%s' % instance.question.exam.title

    get_question_exam.short_description = 'Exam'
