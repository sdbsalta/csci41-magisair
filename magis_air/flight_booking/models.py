from django.db import models
from flight_routes.models import Flight

class Passenger(models.Model):
    passenger_id = models.CharField(primary_key=True, max_length=15, unique=True)
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Others')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    def __str__(self):
        return f"{self.passenger_id} - {self.name}"

class AdditionalItem(models.Model):
    item_id = models.CharField(primary_key=True, max_length=15, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.description

class Booking(models.Model):
    booking_id = models.CharField(primary_key=True, max_length=15, unique=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    booking_date = models.DateField(auto_now_add=True)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name="bookings")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="bookings")
    additional_items = models.ManyToManyField(AdditionalItem, blank=True)

    def __str__(self):
        return f"Booking {self.booking_id} by {self.passenger.name}"