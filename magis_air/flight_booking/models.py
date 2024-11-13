from django.db import models
from django.utils import timezone

class Passenger(models.Model):
    # Generate the passenger ID manually in the save method
    passenger_id = models.CharField(primary_key=True, max_length=15, unique=True)
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Others')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    def save(self, *args, **kwargs):
        if not self.passenger_id:
            # Get the current date in YYMMDD format
            today = timezone.now().strftime('%y%m%d')
            # Find the last passenger to increment the unique sequential part
            last_passenger = Passenger.objects.filter(passenger_id__startswith=f'PAS-{today}').order_by('-passenger_id').first()
            # Extract the numeric part of the last passenger_id or set to 0 if none exists
            last_seq_num = int(last_passenger.passenger_id[-6:]) if last_passenger else 0
            # Increment the sequence number
            seq_num = last_seq_num + 1
            # Ensure that the sequence number is 6 digits
            seq_str = str(seq_num).zfill(6)
            # Construct the passenger_id
            self.passenger_id = f'PAS-{today}-{seq_str}'
        
        super().save(*args, **kwargs)
    
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
    flight = models.ForeignKey('flight_routes.Flight', on_delete=models.CASCADE, related_name="bookings")
    additional_items = models.ManyToManyField(AdditionalItem, blank=True)

    def __str__(self):
        return f"Booking {self.booking_id} by {self.passenger.name}"
