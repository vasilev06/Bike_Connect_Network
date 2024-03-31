from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth import admin as auth_admin

from bike_connect_network.profiles.forms import ProfileUserCreationForm, ProfileUserChangeForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(auth_admin.UserAdmin):
    list_display = ("email", "is_superuser", "is_staff")
    search_fields = ("email",)
    ordering = ("email",)

    form = ProfileUserChangeForm
    add_form = ProfileUserCreationForm

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("last_name", "first_name",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
