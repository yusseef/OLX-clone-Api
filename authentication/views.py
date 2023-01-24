from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class UserCreationView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data.errors, status = status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status = status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)

