# Generated by Django 5.0.3 on 2024-04-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_userstatus_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstatus',
            name='image',
            field=models.ImageField(upload_to='users_status_images'),
        ),
    ]