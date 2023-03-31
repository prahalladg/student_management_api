from django.db import models
from student.models import StudentClass,StudentInfo
from django.core.validators import MaxValueValidator
# Create your models here.


# Create your models here.
'''model for student marks'''
class SubjectMarks(models.Model):
    student_name=models.ForeignKey(StudentInfo,on_delete=models.CASCADE, related_name='student_name')
    Exam_choice =(
    ("Half yearly", "Half yearly"),
    ("Annual", "Annual"))
    exam_type=models.CharField(max_length=20,choices=Exam_choice,default="Half yearly")
    hindi=models.IntegerField(validators=[MaxValueValidator(100)])
    english=models.IntegerField(validators=[MaxValueValidator(100)])
    math=models.IntegerField(validators=[MaxValueValidator(100)])
    science=models.IntegerField(validators=[MaxValueValidator(100)])
    sst=models.IntegerField(validators=[MaxValueValidator(100)])
    total = models.PositiveIntegerField(editable=False,default=0)
    percentage = models.PositiveIntegerField(editable=False,default=0)

    def save(self,**kwargs):
      self.total = self.hindi + self.english + self.math + self.science + self.sst
      self.percentage=self.total / 500 * 100
      return super(SubjectMarks, self).save()

      
    def __str__(self):
        return str(self.exam_type) 
    

    