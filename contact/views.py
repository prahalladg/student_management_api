from django.shortcuts import render
from .models import contactlist
from .models import contactform
from django.core.mail import send_mail
# Create your views here.
def contactus(request):
    '''to show contact infromation and to take the query'''
    if request.method== 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contactformdata=contactform(name=name,email=email,subject=subject,message=message)
        contactformdata.save()
        a=(contactform).objects.all()
        print(a)

        send_mail(
    f'{subject}',
    f'{message}',
    f'{email}',
    ['info@laps.com'],
    fail_silently=False,
)
        
    contactlistdata=contactlist.objects.all()
    context={
        'contactlist':contactlistdata,
        
    }
    return render(request,'contact.html',context)