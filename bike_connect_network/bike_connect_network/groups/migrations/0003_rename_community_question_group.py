# Generated by Django 5.0.3 on 2024-04-03 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_question_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='community',
            new_name='group',
        ),
    ]
