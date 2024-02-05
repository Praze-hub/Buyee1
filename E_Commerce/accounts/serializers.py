from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = User
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=126, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=126, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token')

        read_only_fields = ['token']


class CustomObtainTokenPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user) -> Token:
        token = super().get_token(user)

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = self.user

        return data
