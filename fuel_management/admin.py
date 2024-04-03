# fuel_management/admin.py
from django.contrib import admin
from .models import Vehicle, FuelStation, FuelLog

admin.site.register(Vehicle)
admin.site.register(FuelStation)
admin.site.register(FuelLog)
