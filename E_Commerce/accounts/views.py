from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics, status, response, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from .serializers import RegisterSerializer, LoginSerializer


class AuthUserAPIView(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated)
    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return Response({'user':serializer.data})

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(GenericAPIView):
    serializer_class  = LoginSerializer

    def post(self, request):
        email = request.data.get('email',None)
        password = request.data.get('password', None)
        
        user = authenticate(username=email, password=password)
        print(user)

        if user:
            serializer = self.serializer_class(user)
            print(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        
        return response.Response({'message':'Invalid credentials, try again'}, status=status.HTTP_401_UNAUTHORIZED)


