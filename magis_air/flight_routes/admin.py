from django.contrib import admin
from .models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_id', 'origin', 'destination', 'travel_duration', 'departure_time')
