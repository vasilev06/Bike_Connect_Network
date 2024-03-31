from django.urls import path

from bike_connect_network.web.views import index

urlpatterns = (
    path('', index, name='index'),
)
