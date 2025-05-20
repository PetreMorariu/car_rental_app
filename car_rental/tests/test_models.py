import pytest
from django.contrib.auth import get_user_model
from car_rental.models import Car, Customers, Booking

@pytest.mark.django_db
def test_create_car():
    car = Car.objects.create(make = "Dacia",
                             model = "Spring",
                             car_type = "Truck",
                             year = 2023,
                             rental_price = 45,
                             location = "Timisoara",
                             is_available= True,
                             image = "default.jpg")

    assert car.make == "Dacia"
    assert car.model == "Spring"
    assert car.car_type == "Truck"
    assert car.year == 2023
    assert car.rental_price == 45
    assert car.location == "Timisoara"
    assert car.is_available


@pytest.mark.django_db
def test_create_customer():
    customer = Customers.objects.create(name = "Morariu Petru",
                                        email = "nicu@yahoo.com",
                                        phone_number = "01234567")

    assert customer.name == "Morariu Petru"
    assert customer.email == "nicu@yahoo.com"
    assert customer.phone_number == "01234567"


@pytest.mark.django_db
def test_create_booking():
    car = Car.objects.create(make="Dacia",
                             model="Spring",
                             car_type="Truck",
                             year=2023,
                             rental_price=45,
                             location="Timisoara",
                             is_available=True,
                             image="default.jpg")

    customer = Customers.objects.create(name="Morariu Petru",
                                        email="nicu@yahoo.com",
                                        phone_number="01234567")

    booking = Booking.objects.create(customer = customer,
                                     car = car,
                                     rental_duration = 2)

    assert booking.customer.name == "Morariu Petru"
    assert booking.customer.email == "nicu@yahoo.com"
    assert booking.car.make == "Dacia"
    assert booking.car.model == "Spring"
    assert booking.rental_duration == 2
