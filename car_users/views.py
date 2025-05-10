from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to Log In')
            return redirect('car_rental-home')
    else:
        form = UserRegisterForm()
    return render(request,'car_users/register.html',{'form':form})

def login_user(request):
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('car_rental-home')
            else:
                messages.error(request,
                               f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
                return redirect('login')
        else:
            form = AuthenticationForm()
            return render(request, 'car_users/login.html', {'form': form})

def logout_view(request):
      if request.method == 'POST':
        logout(request)
        return render(request, 'car_users/logout.html')

