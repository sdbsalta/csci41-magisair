from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Passenger, Booking

class PassengerListView(ListView):
    model = Passenger
    template_name = 'flight_booking/passenger_list.html'

class BookingListView(ListView):
    model = Booking
    template_name = 'flight_booking/booking_list.html'

class BookingCreateView(CreateView):
    model = Booking
    fields = ['booking_id', 'total_cost', 'passenger', 'flight', 'additional_items']
    template_name = 'flight_booking/booking_form.html'
    success_url = reverse_lazy('booking_list')

class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['total_cost', 'additional_items']
    template_name = 'flight_booking/booking_form.html'
    success_url = reverse_lazy('booking_list')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'flight_booking/booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')
