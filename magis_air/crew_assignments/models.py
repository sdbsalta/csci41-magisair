from django.db import models

class CrewMember(models.Model):
    crew_id = models.CharField(primary_key=True, max_length=6, unique=True)
    role = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.crew_id} - {self.role}"

class FlightSchedule(models.Model):
    schedule_id = models.CharField(max_length=20, primary_key=True)
    date = models.DateField()
    crew_members = models.ManyToManyField(CrewMember, related_name='crew_assignment_flight_schedules')

    def __str__(self):
        return self.schedule_id