# apps/room/model_forms.py

# Django modules
from django.forms import ModelForm

# Locals
from apps.room.models import Room


# Create your models here.


class RoomModelForm(ModelForm):
	class Meta:
		model = Room
		fields = '__all__'