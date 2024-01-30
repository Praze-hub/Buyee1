from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(max_length=126, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username','email','password',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=126, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email','username','password','token')

        read_only_fields = ['token']

