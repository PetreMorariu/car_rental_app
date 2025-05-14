from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    VEHICLE_TYPES = [
        ('sedan','Sedan'),
        ('suv','Suv'),
        ('truck','Truck')
    ]

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    car_type = models.CharField(max_length=10,choices=VEHICLE_TYPES,default='Sedan')
    year = models.IntegerField()
    rental_price = models.IntegerField(max_length=5)
    location = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.make} {self.model}"
