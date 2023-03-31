from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from student_attendance.api.serializers import StudentAttendanceSerializer
from student_attendance.models import StudentAttendance
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework import serializers


class StudentAttendanceView(viewsets.ViewSet):
    '''
    student Attendance details 
    '''
    permission_classes=[IsAuthenticated]
    
    def list(self,request):                                #list all student attendance details
        attendance = StudentAttendance.objects.all()
        serializer = StudentAttendanceSerializer(attendance,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk):                  #Get particular attendance details using pk
        attendance =StudentAttendance.objects.get(pk=pk)
        serializer = StudentAttendanceSerializer(attendance)
        return Response(serializer.data)
    
    def create(self,request):                          #add attendance 
        serializer = StudentAttendanceSerializer(data=request.data)
        studname =self.request.data['student_name']
        date =self.request.data['date']
            
        if StudentAttendance.objects.filter(student_name=studname,date=date).exists():
            raise serializers.ValidationError({'error':'student Attendance already exist'})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    