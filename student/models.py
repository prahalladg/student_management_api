from django.db import models




'''model for student class'''
class StudentClass(models.Model):
    student_class=models.IntegerField(blank=False)

    def __str__(self):
        return str(self.student_class)


# Create your models here.
''' model to student details'''
class StudentInfo(models.Model):
    student_id=models.CharField(max_length=10, blank=False,unique=True)
    name=models.CharField(max_length=50, blank=False)
    std_class=models.ForeignKey(StudentClass,on_delete=models.CASCADE)
    email=models.EmailField(max_length=50, blank=False)
    contact_number=models.CharField(max_length=10)
    dob=models.DateField(max_length=10, blank=False)
    father_name=models.CharField(max_length=20, blank=False)
    mother_name=models.CharField(max_length=20, blank=False)
    gender_choice =(
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),)
    gender=models.CharField(max_length=10,choices=gender_choice)
    address=models.TextField(max_length=100, blank=False)

    def __str__(self):
        return self.name 


