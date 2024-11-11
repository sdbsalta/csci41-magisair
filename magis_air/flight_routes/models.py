import random
import string
from datetime import datetime, timedelta
from django.db import models

CITY_CHOICES = [
    ('Manila, Philippines', 'Manila, Philippines'),
    ('New York, USA', 'New York, USA'),
    ('London, UK', 'London, UK'),
    ('Tokyo, Japan', 'Tokyo, Japan'),
]

def generate_flight_id():
    # Generate a random alphabetic code of two letters (YY)
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    # Generate a random 4-digit numeric code (XXXX)
    digits = ''.join(random.choices(string.digits, k=4))
    # Combine them to create a unique flight ID
    return f"{letters}{digits}"

class Flight(models.Model):
    flight_id = models.CharField(max_length=6, primary_key=True, unique=True, default=generate_flight_id)
    origin = models.CharField(max_length=255, choices=CITY_CHOICES, default='Manila, Philippines')
    destination = models.CharField(max_length=255, choices=CITY_CHOICES, default='Manila, Philippines')
    
    # Set default value for travel_duration to 00:00:00 (a 0-day, 0-hour, 0-minute duration)
    travel_duration = models.DurationField(default=timedelta(hours=0, minutes=0))
    
    # Set default value for departure_time to 00:00 (midnight)
    departure_time = models.TimeField(default="00:00")
    
    @property
    def formatted_travel_duration(self):
        # Format the travel duration as HH:MM
        hours, remainder = divmod(self.travel_duration.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}"

    @property
    def arrival_time(self):
        # Calculate arrival time based on departure time and travel duration
        if self.departure_time and self.travel_duration:
            # Combine today's date with the departure time
            dep_datetime = datetime.combine(datetime.today(), self.departure_time)
            arrival_datetime = dep_datetime + self.travel_duration
            return arrival_datetime.time()
        return None

    def __str__(self):
        return f"Flight {self.flight_id} from {self.origin} to {self.destination}"

    def save(self, *args, **kwargs):
        # Ensure the flight_id is unique and generated if not provided
        if not self.flight_id:
            self.flight_id = generate_flight_id()
        super().save(*args, **kwargs)
