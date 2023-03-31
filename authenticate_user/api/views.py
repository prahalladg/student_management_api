from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import RegistrationSerializers,UsersSerializers
from rest_framework.authtoken.models import Token
from authenticate_user.models import User


class RegistrationViewSet(viewsets.ViewSet):
    '''
    Register a new user and generate a token for them
    '''
    def create(self, request):
        serializer = RegistrationSerializers(data=request.data)
         
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
        
            data['response'] = "Registration Successful !"
            data['username'] = account.username
            data['email'] = account.email
                
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
    
   
        
class LogoutViewSet(viewsets.ViewSet):
    '''
    Logout the current user and delete the token of the user
    '''
    
    def create(self, request):
        try:
            print(request.user.auth_token)
            request.user.auth_token.delete()
        except (AttributeError):
            pass
        from django.contrib.auth import logout
        logout(request)

        return Response({"success": ("Successfully logged out.")},
                        status=status.HTTP_200_OK)
        
class UserViewSet(viewsets.ViewSet):
    '''
    List all the details of user 
    '''
    def list(self,request):                                     #list all the users details
        users = UsersSerializers(User.objects.all(),many=True)
        return Response(users.data)
    
    def retrieve(self,request,pk=None):                          #Get particular user details
        user =User.objects.get(pk=pk)
        serializer = UsersSerializers(user)
        return Response(serializer.data)
    
    def update(self,request,pk=None):                           #Update a particular user through pk
        user =User.objects.get(pk=pk)
        serializer = UsersSerializers(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,requset,pk):                                #Delete a particular user through pk
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
           