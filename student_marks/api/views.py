from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from student_marks.models import SubjectMarks
from .serializers import StudentMarkSerializers
from django.core.mail import send_mail
from student.models import StudentInfo
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework import serializers


class StudentMarkView(viewsets.ViewSet):
    '''
    Student marks details and send email to particular student
    '''
    permission_classes=[IsAuthenticated]
    
    def list(self,request):                                 #list of all student mark
        student_marks = SubjectMarks.objects.all()
        serializer = StudentMarkSerializers(student_marks,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk):                          #get particular student marks using pk
        student_marks =SubjectMarks.objects.get(pk=pk)
        serializer = StudentMarkSerializers(student_marks)
        return Response(serializer.data)
    
    def create(self,request):                               #add marks and send email to particular student
        serializer = StudentMarkSerializers(data=request.data)
        studname =self.request.data['student_name']
        examty =self.request.data['exam_type']
            
        if SubjectMarks.objects.filter(student_name=studname,exam_type=examty).exists():
            raise serializers.ValidationError({'Error':'student Mark already exist'})
            
        if serializer.is_valid():
            serializer.save()
            sname =serializer.validated_data['student_name']
            student_data=StudentInfo.objects.get(name=sname)
            stud_mail=student_data.email
            stud_name=student_data.name
            stud_id=student_data.student_id
            stud_class=student_data.std_class

            exam_type =serializer.validated_data['exam_type']
            hindi =serializer.validated_data['hindi']
            english =serializer.validated_data['english']
            math =serializer.validated_data['math']
            science =serializer.validated_data['science']
            sst =serializer.validated_data['sst']
            total=int(hindi)+int(english)+int(math)+int(science)+int(sst)
            percentage=int(total) / 500 * 100
            
            mailbody=f"Student Name: {stud_name}\n Student ID:{stud_id}\n Class:{stud_class}\n Here is the marks details \n \nExam type:{exam_type}\n Hindi:{hindi}\n English:{english}\n Math:{math}\n Science:{science}\n SST:{sst}\n Total:{total}\n Percentage:{percentage}% "
            send_mail(f'{"marks"}',f'{mailbody}','info@laps.com',[f'{stud_mail}'],fail_silently=False)
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):                            #update the mark
        student_marks =SubjectMarks.objects.get(pk=pk)
        serializer = StudentMarkSerializers(student_marks,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # def destroy(self,request,pk):
    #     student_marks = get_object_or_404(SubjectMarks,pk=pk)
    #     student_marks.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
