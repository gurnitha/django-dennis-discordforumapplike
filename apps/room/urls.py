# apps/room/urls.py

# Django modules
from django.urls import path

# Locals
from apps.room import views 

app_name = 'room'

urlpatterns = [

    path('room/', views.room, name='room'),
    path('create-room/', views.create_room, name='create_room'),
    path('update-room/<str:pk>/', views.update_room, name='update_room'),
    
]