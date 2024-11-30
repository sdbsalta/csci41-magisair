import random
import string
from django.db import models
from django.utils import timezone

class Passenger(models.Model):
    passenger_id = models.CharField(primary_key=True, max_length=17, unique=True)
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Others')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    def save(self, *args, **kwargs):
        if not self.passenger_id:
            today = timezone.now().strftime('%y%m%d')
            last_passenger = Passenger.objects.filter(passenger_id__startswith=f'PAS-{today}').order_by('-passenger_id').first()
            last_seq_num = int(last_passenger.passenger_id[-6:]) if last_passenger else 0
            seq_num = last_seq_num + 1
            seq_str = str(seq_num).zfill(6)
            self.passenger_id = f'PAS-{today}-{seq_str}'
        
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name 
    
class AdditionalItem(models.Model):
    item_id = models.CharField(primary_key=True, max_length=15, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.description

class Booking(models.Model):
    booking_id = models.CharField(primary_key=True, max_length=16, unique=True)  # Booking ID will be auto-generated
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    booking_date = models.DateField(auto_now_add=True)
    passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE, related_name="bookings")
    flight = models.ForeignKey('flight_routes.Flight', on_delete=models.CASCADE, related_name="bookings")
    additional_items = models.CharField('Additional Item',max_length=255, blank=True)

    def generate_random_sequence(self):
        """Generates a random sequence of 6 uppercase letters."""
        return ''.join(random.choices(string.ascii_uppercase, k=6))

    def save(self, *args, **kwargs):
        if not self.booking_id:
            # Get the current date in YYYYMMDD format
            today = timezone.now().strftime('%y%m%d')
            
            # Generate a random sequence of 6 uppercase letters
            random_seq = self.generate_random_sequence()
            
            # Generate the booking ID in the format XXXXXX-YYYYMMDD
            self.booking_id = f'{random_seq}-{today}'
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.booking_id} for {self.passenger.name}"