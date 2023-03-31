from rest_framework import serializers
from student.models import StudentInfo,StudentClass

class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'
        
class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = '__all__'
        
        