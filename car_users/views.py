from django.shortcuts import render, redirect
from .forms import UserRegisterForm,UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You are now able to Log In')
            return redirect('car_rental-home')
    else:
        form = UserRegisterForm()
    return render(request,'car_users/register.html',{'form':form})