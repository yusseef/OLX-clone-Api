from django.urls import path
from .views import *

urlpatterns = [
    path('', AdvertisesListView.as_view(), name = 'ListAdvertise'),
    path('create/', AdvertiseCreateView.as_view(), name = 'CreateAdvertise'),
    path('advertise/<str:id>/', AdvertisePkView.as_view(), name = 'PkAdvertise'),


]