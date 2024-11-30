from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Flight, generate_flight_id

class FlightListView(ListView):
    model = Flight
    template_name = 'flight_list.html'
    context_object_name = 'data'

    def get_queryset(self):
        origin_filter = self.request.GET.get('origin')
        print("Filtering by origin:", origin_filter)  # Debugging line
        if origin_filter:
            return Flight.objects.filter(origin=origin_filter)
        return Flight.objects.all()

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_form(self):
        # Create and return the form for filtering flights
        from django import forms
        class FlightSearchForm(forms.Form):
            origin = forms.ChoiceField(
                choices=[('Manila, Philippines', 'Manila, Philippines'), ('Tokyo, Japan', 'Tokyo, Japan')],
                required=False,
                label="Select Origin"
            )
        return FlightSearchForm(self.request.GET)

class FlightCreateView(CreateView):
    model = Flight
    fields = ['flight_id', 'origin', 'destination', 'travel_duration_hours', 'travel_duration_minutes', 'departure_time']
    template_name = 'flight_form.html'
    success_url = reverse_lazy('flight_routes:flight_list')

    def get_initial(self):
        """Override the get_initial method to add flight_id to the form."""
        initial = super().get_initial()
        initial['flight_id'] = generate_flight_id()  # Generate a random flight_id
        return initial

    def form_valid(self, form):
        # Assign the generated flight_id when saving the form
        flight = form.save(commit=False)
        flight.flight_id = form.cleaned_data['flight_id']
        flight.save()
        return super().form_valid(form)

class FlightUpdateView(UpdateView):
    model = Flight
    fields = ['flight_id', 'origin', 'destination', 'travel_duration_hours', 'travel_duration_minutes', 'departure_time']
    template_name = 'flight_form.html'
    success_url = reverse_lazy('flight_routes:flight_list')

class FlightDeleteView(DeleteView):
    model = Flight
    template_name = 'flight_confirm_delete.html'
    success_url = reverse_lazy('flight_routes:flight_list')

class FlightDetailView(DetailView):
    model = Flight
    template_name = 'flight_detail.html'
    context_object_name = 'flight'  
