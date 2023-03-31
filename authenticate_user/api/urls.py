from django.contrib import admin
from django.urls import path
from .views import RegistrationViewSet,LogoutViewSet,UserViewSet
from django.urls import path,include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token       # ObtainAuthToken is inbuilt from rest_framework where user  logins



router = routers.DefaultRouter()
router.register(r'register', RegistrationViewSet,basename="Registration")
router.register(r'logout', LogoutViewSet,basename='logout')
router.register(r'users',UserViewSet ,basename='users')
urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token),

]

