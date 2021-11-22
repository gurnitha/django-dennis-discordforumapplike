# apps/account/urls.py

# Django modules
from django.urls import path

# Locals
from apps.account import views 

app_name = 'account'

urlpatterns = [

    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('register/', views.registerUser, name='registerUser'),

]