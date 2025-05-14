from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm
from django.contrib import messages

def home(request):
    cars = Car.objects.all()
    return render(request, 'car_rental/home.html',{'cars':cars})

def detail_view_car(request, car_id:int):
    car = get_object_or_404(Car, id=car_id)
    return render(request,'car_rental/detail_view_car.html',{'car':car})


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

def edit_car(request, car_id: int):
    car = get_object_or_404(Car,id=car_id)

    if request.method == 'POST':
        form = CarForm(request.POST,instance=car)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your car was updated!')
            return redirect('car_rental-home')
    else:
        form = CarForm(instance=car)
    return render(request,'car_rental/edit_car.html', {'form':form, 'car':car})

def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        messages.warning(request, f'The car was deleted!')
        return redirect("car_rental-home")
    return render(request, 'car_rental/confirm_delete.html', {'car': car})















