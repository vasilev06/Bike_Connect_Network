from django.contrib.auth import models as auth_models

from django.db.models import PositiveIntegerField
from django.db import models

from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from bike_connect_network.profiles.managers import ProfileUserManager


class ProfileUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': _('A user with that email already exists')
        },
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = 'email'

    objects = ProfileUserManager()


class Profile(models.Model):
    USER_FIRST_NAME_MAX_LENGTH = 50
    USER_LAST_NAME_MAX_LENGTH = 50

    first_name = models.CharField(
        max_length=USER_FIRST_NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=USER_LAST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )

    age = PositiveIntegerField(
        blank=False,
        null=False,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        ProfileUser,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="profile"
    )
