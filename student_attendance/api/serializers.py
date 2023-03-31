from rest_framework import serializers
from student_attendance.models import StudentAttendance 

class StudentAttendanceSerializer(serializers.ModelSerializer):
    #student_name = serializers.CharField(required=True)
    class Meta:
        model = StudentAttendance
        fields = '__all__'
        
        
        
