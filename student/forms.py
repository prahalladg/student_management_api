from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()
from student.models import StudentInfo
# Create your forms here.


''' form to display student details '''
class NewStudentForm(forms.ModelForm):
	dob = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))

	class Meta:
		model = StudentInfo
		fields = '__all__'
		include=('dob')
		