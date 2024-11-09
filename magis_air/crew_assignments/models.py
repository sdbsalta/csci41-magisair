from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

class CrewMember(models.Model):
    CAPTAIN = 'Captain'
    FIRST_OFFICER = 'First Officer'
    FLIGHT_ATTENDANT = 'Flight Attendant'
    FLIGHT_ENGINEER = 'Flight Engineer'
    
    CREW_ROLE_CHOICES = [
        (CAPTAIN, 'Captain'),
        (FIRST_OFFICER, 'First Officer'),
        (FLIGHT_ATTENDANT, 'Flight Attendant'),
        (FLIGHT_ENGINEER, 'Flight Engineer'),
    ]

    # Crew_ID must be a unique 6-digit number, automatically generated
    crew_id = models.CharField(primary_key=True, max_length=6, unique=True)
    role = models.CharField(max_length=100, choices=CREW_ROLE_CHOICES, blank=False)  # Crew role with choices

    # Many-to-many relationship with FlightSchedule
    flight_schedules = models.ManyToManyField('FlightSchedule', related_name='crew_members_in_schedule')

    def clean(self):
        # Custom validation for crew_id to ensure it's a 6-digit number
        if not self.crew_id.isdigit() or len(self.crew_id) != 6:
            raise ValidationError({'crew_id': 'Crew ID must be a 6-digit number.'})

        if self.role is None:
            raise ValidationError({'role': 'Role cannot be null.'})

    def save(self, *args, **kwargs):
        # Automatically generate crew_id if not provided
        if not self.crew_id:
            last_crew_member = CrewMember.objects.all().order_by('-crew_id').first()
            last_seq_num = int(last_crew_member.crew_id) if last_crew_member else 0
            new_seq_num = last_seq_num + 1
            self.crew_id = str(new_seq_num).zfill(6)  # Ensure it is 6 digits long

        self.clean()  # Call custom validation method before saving
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.crew_id} - {self.role}"

class FlightSchedule(models.Model):
    # Schedule_ID must follow the format SCH-YYMMDD-XXXXXX
    schedule_id = models.CharField(max_length=20, primary_key=True)
    date = models.DateField()

    # Many-to-many relationship with CrewMember
    crew_members = models.ManyToManyField(CrewMember, related_name='flight_schedule_crew_members')

    def save(self, *args, **kwargs):
        if not self.schedule_id:
            today = datetime.today()
            yy = today.strftime('%y')  # Get the last 2 digits of the year
            mmdd = today.strftime('%m%d')  # Get the month and day
            last_schedule = FlightSchedule.objects.all().order_by('-schedule_id').first()
            last_seq_num = int(last_schedule.schedule_id.split('-')[-1]) if last_schedule else 0
            new_seq_num = last_seq_num + 1
            self.schedule_id = f"SCH-{yy}{mmdd}-{str(new_seq_num).zfill(6)}"
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.schedule_id
