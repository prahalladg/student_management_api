from django.contrib import admin
from django.urls import path,include
from contact.api.views import ContactView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact', ContactView, basename='contact')



urlpatterns = [
   
    #path('', ContactView.as_view(), name='contact'),
    path('', include(router.urls)),

]