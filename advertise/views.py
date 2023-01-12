from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from .models import *
from .serializers import *
from django.db.models import Q
from django.db.models.functions import Now
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from authentication.UserPermission import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from django.conf import settings
import stripe

User = get_user_model()
stripe.api_key = settings.STRIPE_SECRET_KEY

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


class AdvertisePkView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, id):
        try:
            return Advertise.objects.get(id=id)
        except Advertise.DoesNotExist:
            return Http404

    def get(self, request, id):
        obj = self.get_object(id)
        serializer = AdvertiseSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        obj = self.get_object(id)
        serializer = AdvertiseSerializer(obj, data=request.data)
        if request.user == obj.owner:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAdvertisesView(APIView):
    
    def get(self, request, user_id):
        user = User.objects.get(pk = user_id)
        user_advertises = Advertise.objects.all().filter(owner = user)
        serializer = AdvertiseSerializer(user_advertises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserAdvertiseDetatilView(APIView):
    def get(self, request, user_id, ad_id):
        user = User.objects.get(pk = user_id)
        user_advertises = Advertise.objects.all().filter(owner = user).filter(id = ad_id)
        serializer = AdvertiseSerializer(user_advertises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StripeCheckoutView(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': 'price_1MPUIXGslCuRnIIuUV1ME6Kn',
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card',],
                mode='payment',
                success_url=settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        except:
            return Response(
                {'error': 'Something went wrong when creating stripe checkout session'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
