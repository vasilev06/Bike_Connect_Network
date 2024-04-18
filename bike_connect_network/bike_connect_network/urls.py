from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include('bike_connect_network.web.urls')),
    path("profile/", include('bike_connect_network.profiles.urls')),
    path("group/", include('bike_connect_network.groups.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
