# Generated by Django 5.1.3 on 2024-11-30 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_booking', '0004_alter_additionalitem_item_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='additional_items',
        ),
        migrations.AddField(
            model_name='booking',
            name='additional_items',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
