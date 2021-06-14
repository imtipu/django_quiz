from django.contrib import admin
from .models import *

from .forms import *


# Register your models here.
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'created', 'updated']
    search_fields = ['title', 'id']


@admin.register(UserExam)
class UserExamAdmin(admin.ModelAdmin):
    list_display = ['user', 'exam', 'created']
    search_fields = ['user', 'exam']
    autocomplete_fields = ('user', 'exam')


class QuestionChoiceInline(admin.TabularInline):
    model = QuestionChoice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'question_type', 'exam', 'created', 'updated']
    search_fields = ['title', 'question_type', ]
    inlines = [QuestionChoiceInline]
    form = QuestionCreateForm

    def get_form(self, request, obj=None, change=True, **kwargs):
        # if obj is None:
        #     self.exclude('choices', 'correct_choices')
        if obj:
            return QuestionChangeForm
        return QuestionCreateForm
        # return super(QuestionAdmin, self).get_form(request, obj, kwargs)


@admin.register(QuestionChoice)
class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'question', 'get_question_exam', 'created', 'updated']

    # prepopulated_fields = {
    #     'question': ('title', )
    # }
    # autocomplete_fields = ('question',)
    def get_question_exam(self, instance):
        return '%s' % instance.question.exam

    get_question_exam.short_description = 'Exam'


@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ['user_exam', 'question', 'get_question_type', 'get_question_exam', 'check_answer',
                    'created', 'updated']
    readonly_fields = [ 'get_question_exam', 'get_question_type', 'check_answer']
    # autocomplete_fields = ('question',)
    form = QuestionAnswerForm

    def get_question_type(self, instance):
        return '%s' % instance.question.get_question_type_display()

    get_question_type.short_description = 'Type'

    def get_question_exam(self, instance):
        return '%s' % instance.question.exam.title

    get_question_exam.short_description = 'Exam'
