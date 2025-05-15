from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='car_rental-home'),
    path('customers/',views.customer_view,name='customers'),
    path('customers/add/',views.customer_add_view,name='add_customers'),
    path('customers/<int:cust_id>/detail_view/',views.customer_detail_view,name='detail_view_customers'),
    path('customers/<int:cust_id>/edit/',views.customer_edit_view,name='edit_customers'),
    path('customers/<int:cust_id>/delete/',views.customer_delete_view,name='delete_customers'),
    path('car/add/',views.add_car,name='add_car'),
    path('car/<int:car_id>/edit/',views.edit_car,name='edit_car'),
    path('car/<int:car_id>/delete/',views.delete_car,name='delete_car'),
    path('car/<int:car_id>/detail_view/',views.detail_view_car,name='detail_view_car'),
    path('bookings/',views.booking_view,name='bookings'),
]