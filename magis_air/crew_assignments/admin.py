from django.contrib import admin
from .models import CrewMember

@admin.register(CrewMember)
class CrewMemberAdmin(admin.ModelAdmin):
    list_display = ('crew_id', 'role')
