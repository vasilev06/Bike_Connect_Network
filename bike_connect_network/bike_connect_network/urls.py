from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include('bike_connect_network.web.urls')),
    path("profile/", include('bike_connect_network.profiles.urls')),
]
