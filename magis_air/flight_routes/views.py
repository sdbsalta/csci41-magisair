from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Flight

class FlightListView(ListView):
    model = Flight
    template_name = 'flight_list.html'

class FlightCreateView(CreateView):
    model = Flight
    fields = ['flight_id', 'origin', 'destination', 'travel_duration', 'departure_time']
    template_name = 'flight_form.html'
    success_url = reverse_lazy('flight_routes:flight_list')

class FlightUpdateView(UpdateView):
    model = Flight
    fields = ['origin', 'destination', 'travel_duration', 'departure_time']
    template_name = 'flight_form.html'
    success_url = reverse_lazy('flight_routes:flight_list')

class FlightDeleteView(DeleteView):
    model = Flight
    template_name = 'flight_confirm_delete.html'
    success_url = reverse_lazy('flight_routes:flight_list')