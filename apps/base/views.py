# apps/base/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.room.models import Room

# Create your views here.

def home(request):
	rooms = Room.objects.all()
	context = {'rooms':rooms}
	return render(request, 'base/index.html', context) 