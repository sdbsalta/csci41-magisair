# Generated by Django 5.1.2 on 2024-12-02 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flight_routes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalItem',
            fields=[
                ('item_id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('passenger_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('additional_items', models.CharField(blank=True, max_length=255, verbose_name='Additional Item')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='flight_routes.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='flight_booking.passenger')),
            ],
        ),
    ]
