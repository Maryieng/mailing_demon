from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clients.urls', namespace='clients')),
    path('mailings/', include('mailings.urls', namespace='mailings')),
    path('letters/', include('letters.urls', namespace='letters')),
    path('reporting/', include('reporting.urls', namespace='reporting')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
