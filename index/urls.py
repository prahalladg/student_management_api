from django.contrib import admin
from django.urls import path,include
from . import views
'''url for home page and about'''
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.aboutus, name='about'),
    
]