# Generated by Django 5.0.3 on 2024-04-10 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_questioncomment_delete_answer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionComment',
        ),
    ]
