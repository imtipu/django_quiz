# Generated by Django 3.2.4 on 2021-06-13 01:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0003_question_question_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswer',
            name='user',
        ),
        migrations.CreateModel(
            name='UserExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('exam', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='userexam_exam', to='quiz.exam')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='exam_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Exam',
                'verbose_name_plural': 'User Exams',
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='questionanswer',
            name='user_exam',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='answer_user_exam', to='quiz.userexam'),
        ),
    ]