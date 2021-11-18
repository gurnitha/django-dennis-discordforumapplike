# apps/room/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.room.model_forms import RoomModelForm

# Create your views here.

def room(request):
	return render(request, 'room/room.html') 


def create_room(request):
	form = RoomModelForm()
	context = {'form':form}
	return render(request, 'room/room_create_update_form.html', context)