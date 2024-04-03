# fuel_management/models.py
from django.db import models

class FuelStation(models.Model):
    # Define your FuelStation model fields here
    # For example:
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    # Add other fields as needed

class Vehicle(models.Model):
    # Define your Vehicle model fields here
    # For example:
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    # Add other fields as needed

class FuelLog(models.Model):
    ward = models.CharField(max_length=100)
    subcounty = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=20)
    fuel_units = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_litre = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    # Add other fields as needed

    def total_amount_spent(self):
        return self.fuel_units * self.price_per_litre
