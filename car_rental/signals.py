from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking, Car

@receiver(post_save,sender=Booking)
def update_car_availability(sender, instance, created, **kwargs):
    if created:
        car = instance.car
        if car.is_available:
            car.is_available = False
            car.save()