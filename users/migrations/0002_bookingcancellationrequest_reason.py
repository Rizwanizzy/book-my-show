# Generated by Django 4.2 on 2023-05-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookingcancellationrequest",
            name="reason",
            field=models.TextField(default=None),
        ),
    ]
