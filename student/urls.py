from django.contrib import admin
from django.urls import path
from . import views

app_name="student"

urlpatterns = [
   path('', views.addstudent, name='addstudent'),
   path('viewstudent/', views.viewstudent, name='viewstudent'),
   path('editstudent/<int:student_id>/', views.editstudent, name='editstudent'),
   path('deletestudent/<int:student_id>/', views.deletestudent, name='deletestudent'),
]