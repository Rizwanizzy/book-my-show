# Generated by Django 4.2 on 2023-05-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0026_show_time_screen_show_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='total_seat_columns',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='screen',
            name='total_seat_rows',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='screen',
            name='unavailable_seats',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
