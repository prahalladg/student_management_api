from django.contrib import admin
from django.urls import path
from . import views

app_name="marks"
urlpatterns = [
   path('', views.addMarks, name='addmarks'),
   path('viewmarks/', views.viewmarks, name='viewmarks'),
   path('editmarks/<int:student_id>/', views.editmarks, name='editmarks'),
   path('deletemarks/<int:student_id>/', views.deletemarks, name='deletemarks'),
]