from django.shortcuts import redirect, render, get_object_or_404
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
            crew_member = get_object_or_404(CrewMember, crew_id=crew_id)
            flight_schedule.crew_members.add(crew_member)  # Add the crew member to the schedule
            crew_member.flight_schedules.add(flight_schedule)
            
        # After saving, redirect to the success URL (flight_schedule list)
        return redirect(self.success_url)

class FlightScheduleUpdateView(UpdateView):
    model = FlightSchedule
    fields = ['schedule_id', 'date', 'flight']
    template_name = 'flight_schedule_form.html'
    success_url = reverse_lazy('flight_schedules:flight_schedule_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add crew members to context (with pre-selected checkboxes for current schedule)
        flight_schedule = self.get_object()
        context['crew_members'] = CrewMember.objects.all()  # All crew members
        context['selected_crew_members'] = flight_schedule.crew_members.all()  # Already selected crew members
        return context
    
    def form_valid(self, form):
        flight_schedule = form.save()

        # Get the selected crew members from the POST data (checkboxes)
        crew_member_ids = self.request.POST.getlist('crew_members')

        # Get the current crew members assigned to this flight schedule
        current_crew_members = flight_schedule.crew_members.all()

        # Remove crew members that were previously selected but are now unchecked
        for crew_member in current_crew_members:
            if str(crew_member.crew_id) not in crew_member_ids:
                flight_schedule.crew_members.remove(crew_member)
                crew_member.flight_schedules.remove(flight_schedule)

        # Add the newly selected crew members
        for crew_id in crew_member_ids:
            crew_member = get_object_or_404(CrewMember, crew_id=crew_id)
            flight_schedule.crew_members.add(crew_member)
            crew_member.flight_schedules.add(flight_schedule)

        return redirect(self.success_url)

class FlightScheduleDeleteView(DeleteView):
    model = FlightSchedule
    template_name = 'flight_schedule_confirm_delete.html'
    success_url = reverse_lazy('flight_schedules:flight_schedule_list')