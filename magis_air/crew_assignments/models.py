from django.db import models

class CrewMember(models.Model):
    crew_id = models.CharField(max_length=6, primary_key=True, unique=True)
    role = models.CharField(max_length=255)

    def __str__(self):
        return f"CrewMember {self.crew_id} - {self.role}"
