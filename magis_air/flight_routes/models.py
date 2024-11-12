import random
import string
from datetime import datetime, timedelta
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

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

    # Separate fields for hours and minutes
    travel_duration_hours = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0), MaxValueValidator(23)],
        help_text="Duration in hours (0-23)",
        error_messages={
            'max_value': 'Travel duration hours cannot exceed 23.',
            'min_value': 'Travel duration hours cannot be less than 0.',
        }
    )
    travel_duration_minutes = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0), MaxValueValidator(59)],
        help_text="Duration in minutes (0-59)",
        error_messages={
            'max_value': 'Travel duration minutes cannot exceed 59.',
            'min_value': 'Travel duration minutes cannot be less than 0.',
        }
    )

    departure_time = models.TimeField(default="00:00")

    @property
    def formatted_travel_duration(self):
        # Format the travel duration as HH:MM
        return f"{self.travel_duration_hours:02}:{self.travel_duration_minutes:02}"

    def arrival_time(self):
        if self.departure_time and (self.travel_duration_hours or self.travel_duration_minutes):
            # Convert departure_time to a timedelta object from the start of the day
            dep_timedelta = timedelta(hours=self.departure_time.hour, minutes=self.departure_time.minute)
            
            # Convert hours and minutes to a timedelta
            travel_timedelta = timedelta(hours=self.travel_duration_hours, minutes=self.travel_duration_minutes)
            
            # Add the travel duration (timedelta) to the departure time
            arrival_timedelta = dep_timedelta + travel_timedelta
            
            # Calculate the arrival hour and minute by extracting them from the timedelta
            arrival_hours = arrival_timedelta.seconds // 3600
            arrival_minutes = (arrival_timedelta.seconds % 3600) // 60
            
            # Format arrival time in HH:MM
            return f"{arrival_hours:02}:{arrival_minutes:02}"

        return None

    def __str__(self):
        return f"Flight {self.flight_id} from {self.origin} to {self.destination}"