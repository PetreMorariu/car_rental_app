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
        if self.instance and self.instance.pk:
            # Editing existing booking
            current_car = self.instance.car
            # Combine available cars with the current car
            available_cars_qs = Car.objects.filter(is_available=True)
            # Use `|` (union) to include current car if it's not in available_cars_qs
            self.fields['car'].queryset = (available_cars_qs | Car.objects.filter(pk=current_car.pk))
        else:
            # Creating new booking, only show available cars
            self.fields['car'].queryset = Car.objects.filter(is_available=True)
