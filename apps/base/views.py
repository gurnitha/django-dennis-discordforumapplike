# apps/base/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.room.models import Room, Topic

# Create your views here.

def home(request):

	# SEARCH

	# Defining search parameter
	q = request.GET.get('q') if request.GET.get('q') != None else ''

	# Get topics by its name within rooms (OneToMany rel)
	# rooms = Room.objects.filter(topic__name=q)
	rooms = Room.objects.filter(topic__name__icontains=q)

	# Get all topics
	topics = Topic.objects.all()

	context = {'rooms':rooms, 'topics':topics}
	return render(request, 'base/index.html', context) 