from django.urls import path, include

from bike_connect_network.profiles.views import (RegistrationUserView, DetailsUserView, LoginUserView, LogoutUserView,
                                                 EditUserView, delete_user_profile)

urlpatterns = (
    path("register", RegistrationUserView.as_view(), name="register_user"),
    path("login/", LoginUserView.as_view(), name="login_user"),
    path("logout/", LogoutUserView.as_view(), name="logout_user"),
    path(
        "<int:pk>/", include([
            path("", DetailsUserView.as_view(), name="details_user"),
            path("edit/", EditUserView.as_view(), name="edit_user"),
            path("delete/", delete_user_profile, name="delete_user"),
        ])
    ),
)
