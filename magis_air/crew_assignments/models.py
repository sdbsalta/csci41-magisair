from django.db import models
from datetime import datetime

class CrewMember(models.Model):
    crew_id = models.CharField(primary_key=True, max_length=6, unique=True)
    role = models.CharField(max_length=100)
    flight_schedules = models.ManyToManyField('FlightSchedule', related_name='crew_members_in_schedule')

    def save(self, *args, **kwargs):
        if not self.crew_id:
            # Find the last crew member to increment the unique sequential part of crew_id
            last_crew_member = CrewMember.objects.all().order_by('-crew_id').first()
            last_seq_num = int(last_crew_member.crew_id) if last_crew_member else 0
            new_seq_num = last_seq_num + 1
            self.crew_id = str(new_seq_num).zfill(6)  # Ensure it is 6 digits long
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.crew_id} - {self.role}"

class FlightSchedule(models.Model):
    schedule_id = models.CharField(max_length=20, primary_key=True)
    date = models.DateField()
    crew_members = models.ManyToManyField(CrewMember, related_name='flight_schedule_crew_members')

    def save(self, *args, **kwargs):
        if not self.schedule_id:
            # Generate the schedule ID in the format SCH-YYMMDD-XXXXXX
            today = datetime.today()
            yy = today.strftime('%y')  # Get the last 2 digits of the year
            mmdd = today.strftime('%m%d')  # Get the month and day
            # Find the last schedule to increment the unique sequential part of schedule_id
            last_schedule = FlightSchedule.objects.all().order_by('-schedule_id').first()
            # Extract the numeric part of the last schedule_id or set to 0 if none exists
            last_seq_num = int(last_schedule.schedule_id.split('-')[-1]) if last_schedule else 0
            # Increment the sequence number for the new schedule
            new_seq_num = last_seq_num + 1
            # Ensure that the sequence number is 6 digits (XXXXXX format)
            self.schedule_id = f"SCH-{yy}{mmdd}-{str(new_seq_num).zfill(6)}"  # format the schedule ID as SCH-YYMMDD-XXXXXX
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.schedule_id
