from rest_framework import serializers
from .models import *

class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','name', 'email', 'password')
    
class UserSigninSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','email', 'password')     
        
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("name",'type','description','file','category')