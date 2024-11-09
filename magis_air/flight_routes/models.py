from django.db import models

class Flight(models.Model):
    flight_id = models.CharField(max_length=6, primary_key=True, unique=True)
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