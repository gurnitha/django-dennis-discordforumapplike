# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Base
    path('', include('apps.base.urls', namespace='base')),

    # Account
    path('', include('apps.account.urls', namespace='account')),

    # Room
    path('', include('apps.room.urls', namespace='room')),
    
    # Admin
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)