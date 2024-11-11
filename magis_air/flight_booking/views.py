from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Passenger, Booking

class PassengerListView(ListView):
    model = Passenger
    template_name = 'passenger_list.html'
    
class PassengerCreateView(CreateView):
    model = Passenger
    fields = ['name', 'birth_date', 'gender'] 
    template_name = 'passenger_form.html'
    success_url = reverse_lazy('flight_booking:passenger_list') 

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'

class BookingCreateView(CreateView):
    model = Booking
    fields = ['booking_id', 'total_cost', 'passenger', 'flight', 'additional_items']
    template_name = 'booking_form.html'

    def get_success_url(self):
        return reverse_lazy('flight_booking:booking_list')

class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['total_cost', 'additional_items']
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_list')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')