from django.contrib import admin
from .models import *
# Register your models here.
class AdAdmin(admin.ModelAdmin):
    list_display = ['description','category',  'location', 'price', 'created_at','expiration_date']
    list_filter = ['location', 'category']
    readonly_fields = ['expiration_date']
admin.site.register(Advertise, AdAdmin)