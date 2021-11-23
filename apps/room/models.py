# apps/room/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import User 


# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Room(models.Model):
	'''Add OneToMany rel between User (Host) and Room models:
	A user can have many rooms, but a room
	belong to only a spesific user'''
	host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	'''Add OneToMany rel between Topic and Room models:
	A topic can have many rooms, but a room
	belong to only a spesific topic'''
	topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	participants = models.ManyToManyField(User, related_name='participants', blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-updated', '-created']
		
	def __str__(self):
		return self.name 


class Message(models.Model):
	'''Add OneToMany rel between User and Message models:
	A use can have many messages, but a message
	belong to only a spesific user'''
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	'''Add OneToMany rel between Room and Message models:
	A room can have many messages, but a message about room
	belong to only a spesific room'''
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	body = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-updated', '-created']

	def __str__(self):
		return self.body[0:50]