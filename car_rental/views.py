from django.shortcuts import render
from .models import Car

def home(request):
    cars = Car.objects.all()
    return render(request, 'car_rental/home.html',{'cars':cars})



