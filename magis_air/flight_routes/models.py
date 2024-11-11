import random
import string
from django.db import models

def generate_flight_id():
    # Generate a random alphabetic code of two letters (YY)
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    # Generate a random 4-digit numeric code (XXXX)
    digits = ''.join(random.choices(string.digits, k=4))
    # Combine them to create a unique flight ID
    return f"{letters}{digits}"

class Flight(models.Model):
    flight_id = models.CharField(max_length=6, primary_key=True, unique=True, default=generate_flight_id)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    travel_duration = models.DurationField()
    departure_time = models.TimeField()

    @property
    def arrival_time(self):
        # Calculate arrival time based on departure time and travel duration
        if self.departure_time and self.travel_duration:
            from datetime import datetime, timedelta
            dep_datetime = datetime.combine(datetime.today(), self.departure_time)
            return (dep_datetime + self.travel_duration).time()
        return None

    def __str__(self):
        return f"Flight {self.flight_id} from {self.origin} to {self.destination}"

    def save(self, *args, **kwargs):
        # Ensure the flight_id is unique and generated if not provided
        if not self.flight_id:
            self.flight_id = generate_flight_id()
        super().save(*args, **kwargs)
