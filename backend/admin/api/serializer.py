from rest_framework import serializers
from .models import *

class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'email', 'password')
    
class UserSigninSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')     

class UserIdSerializer(serializers.ModelSerializer):
    # doubts = DoubtSerializer(many=True, read_only=True)
    # solutions = SolutionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id','name','email','ratings','uploads','views','gender')
