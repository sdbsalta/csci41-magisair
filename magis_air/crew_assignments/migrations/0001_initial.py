# Generated by Django 5.1.2 on 2024-12-01 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flight_schedules', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrewMember',
            fields=[
                ('first_name', models.CharField(max_length=20, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('crew_id', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('role', models.CharField(choices=[('Captain', 'Captain'), ('First Officer', 'First Officer'), ('Flight Attendant', 'Flight Attendant'), ('Flight Engineer', 'Flight Engineer')], max_length=100)),
                ('flight_schedules', models.ManyToManyField(related_name='crew_members_in_schedule', to='flight_schedules.flightschedule')),
            ],
        ),
        migrations.CreateModel(
            name='FlightSchedule',
            fields=[
                ('schedule_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('crew_members', models.ManyToManyField(related_name='flight_schedule_crew_members', to='crew_assignments.crewmember')),
            ],
        ),
    ]
