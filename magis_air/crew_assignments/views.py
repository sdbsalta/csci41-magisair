from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CrewMember

def home(request):
    return render(request, 'home.html') 

class CrewMemberListView(ListView):
    model = CrewMember
    fields = ['crew_id', 'role', 'flight_schedules']
    template_name = 'crew_list.html'

    def get_queryset(self):
        # Prefetch related flight schedules for each crew member to avoid extra queries
        return CrewMember.objects.prefetch_related('flight_schedule_crew_members')

class CrewMemberCreateView(CreateView):
    model = CrewMember
    fields = ['role']
    template_name = 'crew_form.html'
    success_url = reverse_lazy('crew_assignments:crew_list')

class CrewMemberUpdateView(UpdateView):
    model = CrewMember
    fields = ['role']
    template_name = 'crew_form.html'
    success_url = reverse_lazy('crew_assignments:crew_list')

class CrewMemberDeleteView(DeleteView):
    model = CrewMember
    template_name = 'crew_confirm_delete.html'
    success_url = reverse_lazy('crew_assignments:crew_list')
