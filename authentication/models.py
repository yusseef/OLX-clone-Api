from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from .governrates import LOCATIONS

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email is required"))

        email = self.normalize_email(email)
        new_user = self.model(email = email, **extra_fields)
        new_user.set_password(password)
        new_user.save()

        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('SuperUser must have a true is_staff Value'))
            
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('SuperUser must have a true is_superuser Value'))
        
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('SuperUser must have a true is_active Value'))

        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    LOCATIONS = LOCATIONS

    username = models.CharField(max_length = 50, unique = True)
    email = models.EmailField(max_length = 200, unique = True)
    phone_number = PhoneNumberField(null =False, unique = True)
    location = models.CharField(max_length=200, choices=LOCATIONS, null=True, blank = True)
    photo = models.ImageField(upload_to ='photos/%y/%m/%d', default = 'photos/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']
    objects = CustomUserManager()

    def __str__(self):
        return self.username

