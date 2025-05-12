from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='car_rental-home'),
    path('car/add/',views.add_car,name='add_car'),
    path('car/<int:car_id>/edit/',views.edit_car,name='edit_car'),
]