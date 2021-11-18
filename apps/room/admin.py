# apps/room/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.room.models import Room, Topic, Message 

# Register your models here.

admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message)