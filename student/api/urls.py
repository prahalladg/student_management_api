from django.contrib import admin
from django.urls import path,include
from student.api.views import StudentDetailsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentDetails',StudentDetailsView, basename='studentDetails')

urlpatterns = [
    
     path('',include(router.urls))
]