# apps/base/urls.py

# Django modules
from django.urls import path

# Locals
from apps.base import views 

app_name = 'base'

urlpatterns = [

    path('', views.home, name='home'),
    
]