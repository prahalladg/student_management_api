# from rest_framework.response import Response
# from contact.models import contactform
# from contact.api.serializers import ContactSerializer
# from rest_framework.decorators import api_view

# @api_view(['POST'])
# def contact(request):
#     contact=contactform.objects.all()
#     serializer=ContactSerializer(contact,many=True)
#     return Response(serializer.data)

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from contact.api.serializers import ContactSerializer
from rest_framework import status
from contact.models import contactform
from rest_framework import viewsets
from django.core.mail import send_mail




class ContactView(viewsets.ViewSet):
    '''
    contact to school .list all contact details and send email  
    '''
    queryset = contactform.objects.all()
    def list(self, request):                                    #list all details who contact 
        queryset = contactform.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = contactform.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ContactSerializer(user)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            subject =serializer.data['subject']
            message =serializer.data['message']
            email =serializer.data['email']
            send_mail(
        f'{subject}',
        f'{message}',
        f'{email}',
        ['info@laps.com'],
        fail_silently=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
