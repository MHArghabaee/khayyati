from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # صفحه مدیریت Django
    path('', include('account.urls')),
    path('', include('khayyat.urls')),
]
