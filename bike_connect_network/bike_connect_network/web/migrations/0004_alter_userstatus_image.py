# Generated by Django 5.0.3 on 2024-04-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatus',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users_status_images'),
        ),
    ]
