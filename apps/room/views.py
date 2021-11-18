# apps/room/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def room(request):
	return render(request, 'room/room.html') 