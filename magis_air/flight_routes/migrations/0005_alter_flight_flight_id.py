# Generated by Django 5.0.2 on 2024-11-12 10:24

import flight_routes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_routes', '0004_alter_flight_flight_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_id',
            field=models.CharField(default=flight_routes.models.generate_flight_id, editable=False, max_length=6, primary_key=True, serialize=False, unique=True),
        ),
    ]
