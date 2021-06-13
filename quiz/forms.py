from django import forms
from django.core.exceptions import ValidationError
from .models import *


class QuestionAnswerForm(forms.ModelForm):

    def clean(self):
        data = self.cleaned_data
        answers = data.get('answers')
        question = data.get('question')
        choices = question.choice_question
        # QuestionChoice.objects.filter(id__in=)
        # print(question.choice_question.all())
        if data['question'].question_type == 'single' and len(answers) > 1:
            raise ValidationError({'answers': 'You can only select one answer'})

        if not choices.filter(id__in=answers):
            # print(answers)
            raise ValidationError({'answers': 'Select Valid answers for the selected questions'})

    class Meta:
        model = QuestionAnswer
        fields = '__all__'
