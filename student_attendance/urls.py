from django.contrib import admin
from django.urls import path
from . import views

app_name="attendance"
urlpatterns = [
   path('', views.addAttendance, name='addAttendance'),
   path('viewattendance', views.viewattendance, name='viewattendance'),
   path('editattendance/<int:student_id>/', views.editattendance, name='editattendance'),
   path('deleteattendance/<int:student_id>/', views.deleteattendance, name='deleteattendance'),
   path('load_names', views.load_names, name='load_names'),
   
]