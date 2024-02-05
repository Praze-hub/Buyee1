from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics, status, response, permissions, viewsets
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User

from .serializers import RegisterSerializer, LoginSerializer, CustomObtainTokenPairSerializer, UserSerializer


class CustomObtainTokenPairView(TokenObtainPairView):
    """Login with email and password"""

    serializer_class = CustomObtainTokenPairSerializer


class AuthViewSets(viewsets.ModelViewSet):
    """User ViewSets"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    http_method_names = ["get", "post", "patch", "delete"]
    ordering_fields = [
        "created_at",
        "last_login",
        "email",
    ]

    def get_permissions(self):
        derived_permissions = self.permission_classes
        if self.action in [
            "verify_token",
            "retrieve",
            "list",
            "destroy",
            "partial_update",
        ]:
            derived_permissions = [AllowAny]
        return [permission() for permission in derived_permissions]

    @action(
        methods=["POST"],
        detail=False,
        serializer_class=RegisterSerializer,
        permission_classes=[AllowAny],
        url_path="register",
    )
    def register_user(self, request, pk=None):
        """Endpoint for registration"""

    @action(
        methods=["POST"],
        detail=False,
        serializer_class=LoginSerializer,
        permission_classes=[AllowAny],
        url_path="login",
    )
    def login_user(self, request, pk=None):
        """Endpoint for signing in"""


class AuthUserAPIView(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated)

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return Response({'user': serializer.data})


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)
        print(user)

        if user:
            serializer = self.serializer_class(user)
            print(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response({'message': 'Invalid credentials, try again'}, status=status.HTTP_401_UNAUTHORIZED)
