from django.urls import path
from .views import *

urlpatterns = [
    path('', AdvertisesListView.as_view(), name = 'ListAdvertises')
]