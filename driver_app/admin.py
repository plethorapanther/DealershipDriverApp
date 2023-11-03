from django.contrib import admin
from .models import TripEntry, Driver

# Register your models here so they can be edited in admin panel
admin.site.register(TripEntry)
admin.site.register(Driver)