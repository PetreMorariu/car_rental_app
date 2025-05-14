from django import forms
from .models import Car,Customers

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_type','make','model','year','location','rental_price','is_available']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'email', 'phone_number']
