from django.urls import path

from bike_connect_network.web.views import index, UserStatusCreateView, add_comment, like_user_status

urlpatterns = (
    path('', index, name='index'),
    path("create_status/", UserStatusCreateView.as_view(), name='create_status'),
    path('add_comment/<int:status_id>/', add_comment, name='add_comment'),
    path('like/<int:status_id>/', like_user_status, name='like_user_status'),
)
