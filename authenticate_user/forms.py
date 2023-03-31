# from django import forms

# class login_form(forms.Form):
#     email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Enter Email'}))
#     password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))

# class registration_form(forms.Form):
#     user=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Enter User Name'}))
#     email=forms.EmailField()
#     password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
#     conform_password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'placeholder':'Enter password Again'}))


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		

	# def save(self, commit=True):
	# 	user = super(NewUserForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']
	# 	if commit:
	# 		user.save()
	# 	return user