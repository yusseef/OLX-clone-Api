from django.contrib import admin
from .models import *
# Register your models here.
class AdImageInline(admin.TabularInline):
    model = Images
    extra = 5
class AdAdmin(admin.ModelAdmin):
    list_display = ['description','category',  'location', 'price', 'created_at','expiration_date']
    list_filter = ['location', 'category']
    readonly_fields = ['expiration_date']
    inlines = [AdImageInline]
admin.site.register(Advertise, AdAdmin)