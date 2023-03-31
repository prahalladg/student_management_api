from django.contrib import admin
from django.urls import path,include
from student_attendance.api.views import StudentAttendanceView 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('AttendanceDetails',StudentAttendanceView, basename='AttendanceDetails')

urlpatterns = [
    
     path('',include(router.urls))
]
