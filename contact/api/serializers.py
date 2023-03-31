from rest_framework import serializers
from contact.models import contactform


class ContactSerializer(serializers.Serializer):
        id=serializers.IntegerField(read_only=True)
        name=serializers.CharField()
        email=serializers.EmailField()
        subject=serializers.CharField()
        message=serializers.CharField()
        
        def create(self,validated_data):
            return contactform.objects.create(**validated_data)
        