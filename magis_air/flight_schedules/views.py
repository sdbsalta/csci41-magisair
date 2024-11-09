from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import FlightSchedule, CrewMember

class FlightScheduleListView(ListView):
    model = FlightSchedule
    template_name = 'flight_schedule_list.html'

class FlightScheduleCreateView(CreateView):
    model = FlightSchedule
    fields = ['schedule_id', 'date', 'flight']
    template_name = 'flight_schedule_form.html'
    success_url = reverse_lazy('flight_schedules:flight_schedule_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crew_members'] = CrewMember.objects.all()  # Add crew members to context
        return context

    def form_valid(self, form):
        # Save the FlightSchedule first
        flight_schedule = form.save()

        # Get the selected crew members from the POST data (checkboxes)
        crew_member_ids = self.request.POST.getlist('crew_members')  # These are the selected crew member IDs

        # Add the selected crew members to the flight schedule
        for crew_id in crew_member_ids:
            crew_member = CrewMember.objects.get(id=crew_id)  # Get the crew member by ID
            flight_schedule.crew_members.add(crew_member)  # Add the crew member to the schedule

        # After saving, redirect to the success URL (flight_schedule list)
        return redirect(self.success_url)

class FlightScheduleUpdateView(UpdateView):
    model = FlightSchedule
    fields = ['schedule_id', 'date']
    template_name = 'flight_schedule_form.html'
    success_url = reverse_lazy('flight_schedules:flight_schedule_list')

class FlightScheduleDeleteView(DeleteView):
    model = FlightSchedule
    template_name = 'flight_schedule_confirm_delete.html'
    success_url = reverse_lazy('flight_schedules:flight_schedule_list')