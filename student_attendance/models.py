from django.db import models
from student.models import StudentClass,StudentInfo
# Create your models here.

    
'''model for attendance details'''
class StudentAttendance(models.Model):
    #student_class=models.ForeignKey(StudentClass,on_delete=models.CASCADE)
    student_name=models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    attendance_choice=(("Present","Present"),("Absent","Absent"))
    attendance=models.CharField(max_length=10,choices=attendance_choice)
    date=models.DateField()

    def __str__(self):
        return str(self.student_name)