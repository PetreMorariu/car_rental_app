from django.db.models.signals import pre_save, post_save,post_delete
from django.dispatch import receiver
from django.db import transaction
from .models import Booking, Car

@receiver(pre_save, sender=Booking)
def store_previous_car(sender, instance, **kwargs):
    if instance.pk:
        # Fetch the previous booking from the database
        previous_booking = Booking.objects.get(pk=instance.pk)
        # Attach previous car to the instance for later comparison
        instance._previous_car = previous_booking.car
    else:
        # New booking, no previous car
        instance._previous_car = None

@receiver(post_save, sender=Booking)
def update_car_availability(sender, instance, created, **kwargs):
    with transaction.atomic():
        if created:
            # For new bookings, mark the car as unavailable
            car = instance.car
            if car.is_available:
                car.is_available = False
                car.save()
        else:
            # For updates, check if the car has changed
            old_car = getattr(instance, '_previous_car', None)
            new_car = instance.car

            if old_car != new_car:
                # Make old car available again if it was unavailable
                if old_car and not old_car.is_available:
                    old_car.is_available = True
                    old_car.save()

                # Make new car unavailable if it is available
                if new_car.is_available:
                    new_car.is_available = False
                    new_car.save()


@receiver(post_delete, sender=Booking)
def free_car_on_delete(sender, instance, **kwargs):
    car = instance.car
    if not car.is_available:
        car.is_available = True
        car.save()