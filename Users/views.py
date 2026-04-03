from django.shortcuts import render
from Users.Usersapi.throttling import LoginThrottle
from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth.models import User
from Users.Usersapi.serializers import RegistrationSerializer, UserProfileSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from Users.Usersapi.permissions import LogoutPermission, UserModify
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class UserViewSet(APIView):
    permission_classes = [UserModify]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data["password"] != serializer.validated_data["password2"]:
                return Response({"error": "Passwords do not match"}, status=400)
            if serializer.validated_data["type"] not in ["employee", "employer"]:
                return Response({"error": "Invalid user type make (Employee or Employer)"}, status=400)
            if User.objects.filter(username=serializer.validated_data["username"]).exists():
                return Response({"error": "Username already exists"}, status=400)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class LogoutView(APIView):
    permission_classes = [LogoutPermission]
    def post(self, request):
        return Response({"message": "Logged out successfully."})
    
class LoginView(APIView):
    throttle_classes = [LoginThrottle]
    def post(self, request):
        user=User.objects.filter(username=request.data.get("username")).first()
        if user is None or not user.check_password(request.data.get("password")):
            return Response({"error": "Invalid credentials"}, status=401)
        token = RefreshToken.for_user(user)
        data={
            "refresh": str(token),
            "access": str(token.access_token)
        }
        return Response(data, status=200)
    
class UserProfileView(APIView):
    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        if request.user.is_authenticated:
            return Response(serializer.data)
        elif not request.user.is_authenticated:
            return Response({"error": "Authentication credentials were not provided."}, status=401)
    
