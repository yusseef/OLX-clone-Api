from django.db import models
from datetime import date
from django.contrib.auth import get_user_model
from .categories import CATEGORY
from authentication.governrates import LOCATIONS
from .dates import Expire_date
User = get_user_model()
# Create your models here.
class Advertise(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="advertise")
    category = models.CharField(max_length= 200, choices = CATEGORY)
    location = models.CharField(max_length= 200, choices = LOCATIONS)
    description = models.TextField(max_length=600)
    price = models.FloatField(max_length=100)
    expiration_date  = models.DateField(default = Expire_date, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    #is_active

    class Meta:
        ordering = ['created_at']


    def __str__(self):
        return self.category

class Images(models.Model):
    advertise = models.ForeignKey(Advertise, related_name= 'images', on_delete = models.CASCADE)
    image  = models.ImageField(blank=True, null = True, upload_to='uploads/ads' ,default = '')