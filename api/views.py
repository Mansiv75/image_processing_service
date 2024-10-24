from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegisterSerializer, UserSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        username= request.data.get('username') 
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh= RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error':'Invalid credentials'}, status=400)
# Create your views here.
