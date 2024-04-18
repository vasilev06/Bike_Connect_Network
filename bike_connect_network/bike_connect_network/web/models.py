from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image

UserModel = get_user_model()


class UserStatus(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    status = models.TextField()

    image = models.ImageField(
        upload_to='users_status_images',
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    likes = models.ManyToManyField(
        UserModel,
        related_name='status_likes',
        blank=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        desired_width = 600
        aspect_ratio = img.width / img.height
        desired_height = int(desired_width / aspect_ratio)
        output_size = (desired_width, desired_height)
        img.thumbnail(output_size)
        img.save(self.image.path)

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    MAX_LENGTH_TEXT = 300

    status = models.ForeignKey(
        UserStatus,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    text = models.TextField(
        max_length=MAX_LENGTH_TEXT,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
