from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth import get_user_model
#from authenticate_user.models import User
user = get_user_model()

def authregistration(request):
	'''for new user registration '''
	if request.method == "POST":
		user_form = NewUserForm(request.POST)
		if user_form.is_valid():
			user = user_form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		else:
			print(user_form.errors)
		messages.error(request, user_form.errors, "Unsuccessful registration. Invalid information.")
	user_form = NewUserForm()
	return render (request, 'authenticate/registration.html', context={"register":user_form})



def authlogin(request):
	'''for login '''
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("profile")
			else:
				messages.error(request,"Invalid Email or password.")
		else:
			messages.error(request,"Invalid Email or password.")
	form = AuthenticationForm()
	return render(request, 'authenticate/login.html', context={"login":form})

def authlogout(request):
    '''for logout '''
    logout(request)
    messages.success(request,'Logout Successfully')
    return redirect('login')

def forgotpassword(request):
    return render(request,'authenticate/forget.html')


