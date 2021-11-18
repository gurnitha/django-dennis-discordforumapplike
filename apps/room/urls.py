# apps/room/urls.py

# Django modules
from django.urls import path

# Locals
from apps.room import views 

app_name = 'room'

urlpatterns = [

    path('room/', views.room, name='room'),
    
]