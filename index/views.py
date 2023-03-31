from django.shortcuts import render
from .models import about
from .models import slider,notice
# Create your views here.

def home(request):
    '''Here we get the silder details'''
    sliderdata=slider.objects.all()
    noticedata=notice.objects.all()
    context={
        'slider':sliderdata ,
        'notice':noticedata
    }
    return render(request,'index.html',context)

def aboutus(request):
    '''Here we get the about details and rendering to html page'''
    aboutdata=about.objects.all()
    context={'about':aboutdata}
    return render(request,'about.html',context)

