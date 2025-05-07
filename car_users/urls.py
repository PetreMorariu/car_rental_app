from django.urls import path
from car_users import views

urlpatterns = [
    path('/register',views.register, name='register'),
]