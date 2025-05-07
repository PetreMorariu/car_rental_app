from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='car_rental-home')
]