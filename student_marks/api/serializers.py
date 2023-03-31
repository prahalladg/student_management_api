from rest_framework import serializers
from student_marks.models import SubjectMarks
from student.models import StudentInfo
from student.api.serializers import StudentInfoSerializer

class StudentMarkSerializers(serializers.ModelSerializer):
    #student_name = serializers.StringRelatedField(read_only=True)
    #student_name =StudentInfoSerializer()
    #student_name = serializers.CharField(required=True)
    #student_name=serializers.RelatedField(read_only=True,many=True)
    
    
    
    class Meta:
        model = SubjectMarks
        fields = '__all__'
        #fields =['student_name','hindi','english','math','science','sst']
        
        
    
    