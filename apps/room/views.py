# apps/room/views.py

# Django modules
from django.shortcuts import render, redirect

# Locals
from apps.room.model_forms import RoomModelForm
from apps.room.models import Room

# Create your views here.

def room(request):
	return render(request, 'room/room.html') 

# ------------ROOM CRUD------------

def create_room(request):
	form = RoomModelForm()

	if request.method == 'POST':
		# print(request.POST)
		form = RoomModelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('base:home')

	context = {'form':form}
	return render(request, 'room/room_create_update_form.html', context)


def update_room(request, pk):
	room = Room.objects.get(id=pk)
	form = RoomModelForm(instance=room)

	if request.method == 'POST':
		form = RoomModelForm(request.POST, instance=room)
		if form.is_valid():
			form.save()
			return redirect('base:home')

	context = {'form':form}
	return render(request, 'room/room_create_update_form.html', context)


def delete_room(request, pk):
	
	room = Room.objects.get(id=pk)
	
	if request.method == 'POST':
		room.delete()
		return redirect('base:home')

	context = {'obj':room}
	return render(request, 'room/delete_confirm.html', context)

# ------------ROOM CRUD------------
