# apps/base/views.py

# Django modules
from django.shortcuts import render

# Locals

# Create your views here.

# NOTE: Do not name login to avoic conflic
#       with the build in Django modules
def loginPage(request):
	return render(request, 'account/register_login_form.html')