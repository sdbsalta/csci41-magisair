from django import forms
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
    


class BookingIDSearchForm(forms.Form):
    booking_id = forms.CharField(
        min_length=13,
        max_length=13,
        required=False,
        label="Type Booking ID"
    )

class PassengerSearchForm(forms.Form):
    passenger = forms.CharField(
        min_length=10,
        max_length=160,
        required=False,
        label="Type Passenger Name"
    )

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
    
    def get_queryset(self):
        booking_id_filter = self.request.GET.get('booking_id')
        passenger_filter = self.request.GET.get('passenger')

        queryset = Booking.objects.all()

        if booking_id_filter:
            queryset = queryset.filter(booking_id=booking_id_filter)

        if passenger_filter:
            queryset = queryset.filter(passenger__name__icontains=passenger_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking_id_form'] = BookingIDSearchForm(self.request.GET)
        context['passenger_id_form'] = PassengerSearchForm(self.request.GET)
        return context

class BookingCreateView(CreateView):
    model = Booking
    fields = ['total_cost', 'passenger', 'flight', 'additional_items']  # Omit 'booking_id' from the form
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
