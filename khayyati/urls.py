from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),  # صفحه مدیریت Django
    path('', include('account.urls')),
    path('', include('khayyat.urls')),
]
# Debug mode-specific URL patterns for serving media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
