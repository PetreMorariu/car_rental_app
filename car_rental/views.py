from django.shortcuts import render,redirect
from .models import Car
from .forms import CarForm
from django.contrib import messages

def home(request):
    cars = Car.objects.all()
    return render(request, 'car_rental/home.html',{'cars':cars})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'The car was added to the Fleet!')
            return redirect('car_rental-home')
        else:
            messages.error(request,f'Correct the issues!')
            return render(request, 'car_rental/add_car.html', {'form': form})
    else:
        form = CarForm()
        return render(request, 'car_rental/add_car.html', {'form': form})