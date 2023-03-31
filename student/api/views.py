from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from student.api.serializers import StudentInfoSerializer
from student.models import StudentInfo
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

class StudentDetailsView(viewsets.ViewSet):
    '''
    List all the student details and perform CRUD operation
    '''
    permission_classes=[IsAuthenticated]                             #permission 
    
    queryset = StudentInfo.objects.all()
    def list(self, request):                                           #list all the student details
        students = StudentInfo.objects.all()
        serializer = StudentInfoSerializer(students, many=True)
        return Response(serializer.data)
    
    def create(self, request):                                         #Register new student     
        serializer = StudentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):                               #Get details of a particular student
        student = get_object_or_404(StudentInfo, pk=pk)
        serializer = StudentInfoSerializer(student)
        return Response(serializer.data)
    
    
    def partial_update(self, request, pk=None):                         #update details of particular student
        student = get_object_or_404(StudentInfo, pk=pk)
        serializer = StudentInfoSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):                                  #Delete a particular student using pk
        student = get_object_or_404(StudentInfo, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        