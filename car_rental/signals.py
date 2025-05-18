from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Booking, Car

# To temporarily store previous car before save
import threading

_thread_locals = threading.local()

@receiver(pre_save, sender=Booking)
def store_previous_car(sender, instance, **kwargs):
    if instance.pk:
        previous_booking = Booking.objects.get(pk=instance.pk)
        # Store previous car object
        _thread_locals.prev_car = previous_booking.car
    else:
        _thread_locals.prev_car = None

@receiver(post_save, sender=Booking)
def update_car_availability(sender, instance, created, **kwargs):
    if created:
        # New booking: mark the car as unavailable
        car = instance.car
        if car.is_available:
            car.is_available = False
            car.save()
    else:
        # Existing booking was updated
        old_car = getattr(_thread_locals, 'prev_car', None)
        new_car = instance.car

        if old_car != new_car:
            # Make old car available again
            if old_car and not old_car.is_available:
                old_car.is_available = True
                old_car.save()

            # Mark new car as unavailable
            if new_car.is_available:
                new_car.is_available = False
                new_car.save()