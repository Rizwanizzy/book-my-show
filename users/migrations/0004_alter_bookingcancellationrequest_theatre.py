# Generated by Django 4.2 on 2023-05-30 08:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_bookingcancellationrequest_theatre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookingcancellationrequest",
            name="theatre",
            field=models.CharField(default=None, max_length=50),
        ),
    ]
