from django import forms
from .models import Car,Customers,Booking

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_type','make','model','year','location','rental_price','is_available']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'email', 'phone_number']

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['customer', 'car', 'booking_date','rental_duration']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'car', 'booking_date', 'rental_duration']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(is_available=True)
