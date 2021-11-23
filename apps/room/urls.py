# apps/room/urls.py

# Django modules
from django.urls import path

# Locals
from apps.room import views 

app_name = 'room'

urlpatterns = [

    path('room/<str:pk>/', views.room_single, name='room_single'),
    path('create-room/', views.create_room, name='create_room'),
    path('update-room/<str:pk>/', views.update_room, name='update_room'),
    path('delete-room/<str:pk>/', views.delete_room, name='delete_room'),
    path('delete-message/<str:pk>/', views.delete_message, name='delete_message'),
    
]