from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('login/', views.authlogin, name='login'),
    path('registration/', views.authregistration, name='registration'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('logout/', views.authlogout, name='logout'),

]