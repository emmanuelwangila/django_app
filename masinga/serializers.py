from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(max_length=70, min_length=8, write_only=True)

    class Meta:
        model= User
        fields=['email', 'password', 'username']


    def validate(self, attrs):
        email= attrs.get('email', '')
        username= attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('Username should only have alphanumeric chars')
        return attrs
    

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)

