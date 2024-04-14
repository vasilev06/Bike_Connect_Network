from django.urls import path, include

from bike_connect_network.groups.views import GroupListView, GroupDetailView, GroupCreateView, GroupJoinView, \
    GroupLeaveView, EventCreateView

urlpatterns = (
    path("", GroupListView.as_view(), name="list_groups"),
    path("<int:pk>/", include([
        path("details/", GroupDetailView.as_view(), name="detail_group"),
        path("join/", GroupJoinView.as_view(), name='join_group'),
        path("leave/", GroupLeaveView.as_view(), name='leave_group'),
        path("event/", EventCreateView.as_view(), name='create_event'),
    ])),
    path("create/", GroupCreateView.as_view(), name="create_group"),
)
