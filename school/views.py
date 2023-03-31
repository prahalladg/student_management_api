from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def school(request):
    return HttpResponse("this is school page")

def profile(request):
    return render(request,'school/profile.html')
