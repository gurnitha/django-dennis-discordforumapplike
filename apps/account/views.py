# apps/base/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Locals

# Create your views here.

# NOTE: Do not name login to avoic conflic
#       with the build in Django modules
def loginPage(request):
	page = 'login'

	# Restrict user from going to loginPage
	if request.user.is_authenticated:
		return redirect('base:home')

	# 1. If POST request, get the input data
	#    that is the username and password
	if request.method == 'POST':
		# (Optional) Print out the input in the terminal
		# print(request.POST)

		username = request.POST['username'].lower()
		password = request.POST['password']

		# 2. Use 'try block' to check if the input data exist 
		# or not in the db, then return user
		try:
			user = User.objects.get(username=username)
		# 3. If user does not exist in db
		#    or the credentials is not correct
		#    show flash message
		except:
			messages.error(request, 'Username does not exitst!')

		# 4. If user exists, authenticate it, then return user
		user = authenticate(
			request,
			username=username,
			password=password)

		# 5. If authenticated (user does exist), log the user in
		# and redirect him to any page you want
		if user is not None:
			# This login will create session in the db
			# and the session will use it in the browser
			login(request, user)
			return redirect('base:home')

		# 6. If user exist, but its credentials incorrect
		else:
			messages.error(request, 'Username OR password is incorrect. Try it again ...')
			return redirect('account:loginPage')

	context = {
		'page':page
	}
	return render(request, 'account/register_login_form.html', context)



def logoutUser(request):
	logout(request)
	return redirect('base:home')



def registerUser(request):

	form = UserCreationForm()

	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			# It means to access right away the
			# user that just created
			user = form.save(commit=False)
			user.username = user.username.lower()
			user.save()
			# If register success, log in the user, then
			# redirect him to the home page
			login(request, user)
			return redirect('base:home')

		else:
			messages.error(request, 'An error occurred during the registration!')


	context = {
		'form':form,
	}
	return render(request, 'account/register_login_form.html', context)

