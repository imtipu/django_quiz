from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.utils.functional import cached_property


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
    choices = models.ManyToManyField('quiz.QuestionChoice', related_name='question_choices', blank=True)
    correct_choices = models.ManyToManyField('quiz.QuestionChoice', related_name='question_answer_choices', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Exam: % s - %s' % (self.exam.pk, self.title)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class QuestionChoice(models.Model):
    question = models.ForeignKey('quiz.Question', on_delete=models.CASCADE, default=None,
                                 related_name='choice_question')
    title = models.CharField(max_length=250, null=False)
    # is_answer = models.BooleanField(default=False)

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
    answers = models.ManyToManyField('quiz.QuestionChoice')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def check_answer(self):
        q1 = self.question.correct_choices.all()
        q2 = self.answers.all()
        if not q1.count() < 1 and not q2.count() < 1:
            return set(q1) == set(q2)
        return False

    def __str__(self):
        return '%s' % self.question.title[:50]

    class Meta:
        ordering = ('created',)
        verbose_name = 'Question Answer'
        verbose_name_plural = 'Question Answers'
