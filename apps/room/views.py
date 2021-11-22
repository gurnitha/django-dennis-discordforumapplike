# apps/room/views.py

# Django modules
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Locals
from apps.room.model_forms import RoomModelForm
from apps.room.models import Room

# Create your views here.

def room(request):
	return render(request, 'room/room.html') 

# ------------ROOM CRUD------------


@login_required(login_url='account:loginPage')
def create_room(request):
	form = RoomModelForm()

	# Restrict NOT-OWNER of the room to update
	if request.user != room.host:
		return HttpResponse('You are not allowed here!')
		
	if request.method == 'POST':
		# print(request.POST)
		form = RoomModelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('base:home')

	context = {'form':form}
	return render(request, 'room/room_create_update_form.html', context)


@login_required(login_url='account:loginPage')
def update_room(request, pk):
	room = Room.objects.get(id=pk)
	form = RoomModelForm(instance=room)

	# Restrict NOT-OWNER of the room to update
	if request.user != room.host:
		return HttpResponse('You are not allowed here!')

	if request.method == 'POST':
		form = RoomModelForm(request.POST, instance=room)
		if form.is_valid():
			form.save()
			return redirect('base:home')

	context = {'form':form}
	return render(request, 'room/room_create_update_form.html', context)


@login_required(login_url='account:loginPage')
def delete_room(request, pk):
	
	room = Room.objects.get(id=pk)

	# Restrict NOT-OWNER of the room to update
	if request.user != room.host:
		return HttpResponse('You are not allowed here!')

	if request.method == 'POST':
		room.delete()
		return redirect('base:home')

	context = {'obj':room}
	return render(request, 'room/delete_confirm.html', context)

# ------------ROOM CRUD------------
