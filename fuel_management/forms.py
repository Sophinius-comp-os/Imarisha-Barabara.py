# fuel_management/forms.py
from django import forms
from .models import FuelLog

class FuelLogForm(forms.ModelForm):
    class Meta:
        model = FuelLog
        fields = ['ward', 'subcounty', 'equipment', 'number_plate', 'fuel_units', 'price_per_litre', 'date']
