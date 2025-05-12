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
            messages.success(request, f'Your recipe has been created!')
            return redirect('car_rental-home')
        else:
            messages.error(f'Correct the issues!')
            return redirect(request,'car_rental/add_car.html',{'form':form})
    else:
        form = CarForm()
        return redirect(request, 'car_rental/add_car.html', {'form': form})