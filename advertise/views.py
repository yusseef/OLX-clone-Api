from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.db.models import Q
from django.db.models.functions import Now
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class AdvertisesListView(APIView):
    def get(self, request):
        advertises = Advertise.objects.filter(Q (expiration_date__gt = Now()))
        serializer = AdvertiseSerializer(advertises, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class AdvertiseCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = AdvertiseSerializer(data=request.data)
        user = request.user
        if serializer.is_valid():
            print(user)
            serializer.save(owner = user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

