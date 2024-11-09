from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CrewMember

class CrewMemberListView(ListView):
    model = CrewMember
    template_name = 'crew_list.html'

class CrewMemberCreateView(CreateView):
    model = CrewMember
    fields = ['crew_id', 'role']
    template_name = 'crew_form.html'
    success_url = reverse_lazy('crew_list')

class CrewMemberUpdateView(UpdateView):
    model = CrewMember
    fields = ['role']
    template_name = 'crew_form.html'
    success_url = reverse_lazy('crew_list')

class CrewMemberDeleteView(DeleteView):
    model = CrewMember
    template_name = 'crew_confirm_delete.html'
    success_url = reverse_lazy('crew_list')
