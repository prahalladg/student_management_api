from django.urls import path
from . import views

urlpatterns = [
    path('', views.school),
    path('profile', views.profile , name='profile'),
    
]