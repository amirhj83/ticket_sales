from django.db import models
from django.contrib.auth.models import User


class Flight (models.Model):
    flight_number = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

