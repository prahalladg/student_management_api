from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from student.models import StudentClass,StudentInfo
User=get_user_model()
from .models import StudentAttendance

# Create your forms here.

class AllStudentAttendance(forms.ModelForm):
    attendance_choice=(("Present","Present"),("Absent","Absent"))
    date=forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    attendance= forms.CharField(widget=forms.RadioSelect(choices=attendance_choice))
    class Meta:
        model=StudentAttendance
        fields = '__all__'
        include=('date','attendance')
        
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].queryset = StudentInfo.objects.none()

           
            if 'student_class' in self.data:
                try:
                    class_id = int(self.data.get('student_class'))
                    self.fields['student_name'].queryset = StudentInfo.objects.filter(std_class=class_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            

