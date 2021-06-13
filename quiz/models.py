from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

class Exam(models.Model):
    title = models.CharField(max_length=250, null=False)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.title

    @property
    def total_questions(self):
        return self.exam_questions.count()

    class Meta:
        ordering = ('title',)
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'


QUESTION_TYPE_CHOICES = (
    ('multiple', 'Multiple'),
    ('single', 'Single'),
)


class Question(models.Model):
    exam = models.ForeignKey('quiz.Exam', on_delete=models.CASCADE, related_name='exam_questions')

    title = models.CharField(max_length=250, null=False)
    question_type = models.CharField(choices=QUESTION_TYPE_CHOICES, default='single', max_length=20)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class QuestionChoice(models.Model):
    question = models.ForeignKey('quiz.Question', on_delete=models.CASCADE, related_name='choice_question')
    title = models.CharField(max_length=250, null=False)
    is_answer = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Question Choice'
        verbose_name_plural = 'Question Choices'


class UserExam(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, default=None, null=False,
                             related_name='exam_user')

    exam = models.ForeignKey('quiz.Exam', on_delete=models.CASCADE, default=None, null=False,
                             related_name='userexam_exam')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.exam.title

    class Meta:
        ordering = ('created',)
        verbose_name = 'User Exam'
        verbose_name_plural = 'User Exams'

        unique_together = ('user', 'exam',)


class QuestionAnswer(models.Model):
    user_exam = models.ForeignKey('quiz.UserExam', on_delete=models.CASCADE, default=None, null=False,
                                  related_name='answer_user_exam')
    question = models.ForeignKey('quiz.Question', on_delete=models.CASCADE, related_name='answer_question')
    # choice = models.ForeignKey('quiz.QuestionChoice', on_delete=models.CASCADE, related_name='answer_choice')
    answers = models.ManyToManyField('quiz.QuestionChoice')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def check_answer(self):
        if self.question.question_type == 'single':
            return self.question.choice_question.filter(is_answer=True).count() == 1
        return self.question.choice_question.filter(is_answer=True, question__question_type='multiple').exists()

    # def get_answers(self):
    #     return self.choice_set.filter(is_answer=True)

    def __str__(self):
        return '%s' % self.question.title[:50]

    # def clean(self):
    #     print(self.answers.all())
        # if self.pk is None:
        #     check_ans_exist = QuestionAnswer.objects.filter(question=self.question, user_exam=self.user_exam).exists()
        #     print(check_ans_exist)
        #     if self.question.question_type == 'single' and check_ans_exist:
        #         raise ValidationError({'answers': 'You have already answered this question'})
        # elif self.pk:
        #     if self.question.question_type == 'single' and self.answers.count() > 1:
        #         raise ValidationError({'answers': 'You can only select one answer'})

    class Meta:
        ordering = ('created',)
        verbose_name = 'Question Answer'
        verbose_name_plural = 'Question Answers'
