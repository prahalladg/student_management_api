from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from student_marks.models import SubjectMarks
from django.contrib.auth import get_user_model
from .models import StudentInfo
User=get_user_model()
# Create your forms here.


'''student marks form'''
class studentMarksForm(forms.ModelForm):

	class Meta:
		model = SubjectMarks
		fields = '__all__'
		
		