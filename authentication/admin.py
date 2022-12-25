from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'location', 'created_at', 'updated_at']
    list_filter = ['location']
admin.site.register(User, UserAdmin)
# Register your models here.
