from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Flight

class FlightScheduleListView(ListView):
    model = Flight
    template_name = 'flights_schedules/flight_schedule_list.html'

class FlightScheduleCreateView(CreateView):
    model = Flight
    fields = ['flight_id', 'origin', 'destination', 'travel_duration', 'departure_time']
    template_name = 'flights_schedules/flight_schedule_form.html'
    success_url = reverse_lazy('flight_schedule_list')

class FlightScheduleUpdateView(UpdateView):
    model = Flight
    fields = ['origin', 'destination', 'travel_duration', 'departure_time']
    template_name = 'flights_schedules/flight_schedule_form.html'
    success_url = reverse_lazy('flight_schedule_list')

class FlightScheduleDeleteView(DeleteView):
    model = Flight
    template_name = 'flights_schedules/flight_schedule_confirm_delete.html'
    success_url = reverse_lazy('flight_schedule_list')