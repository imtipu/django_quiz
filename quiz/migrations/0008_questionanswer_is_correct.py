# Generated by Django 3.2.4 on 2021-06-13 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_remove_questionanswer_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionanswer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]
