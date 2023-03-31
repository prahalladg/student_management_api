from django.contrib import admin
from django.urls import path,include
from student_marks.api.views import StudentMarkView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('MarkDetails',StudentMarkView, basename='MarkDetails')

urlpatterns = [
    
     path('',include(router.urls))

]