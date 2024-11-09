from django.db import models
from crew_assignments.models import CrewMember
from flight_routes.models import Flight

class FlightSchedule(models.Model):
    schedule_id = models.CharField(primary_key=True, max_length=15, unique=True)
    date = models.DateField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    crew_members = models.ManyToManyField(CrewMember, related_name="schedules_for_member")  # Unique related_name

    def __str__(self):
        return f"{self.schedule_id} - {self.flight.flight_id} on {self.date}"