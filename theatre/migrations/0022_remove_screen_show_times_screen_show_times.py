# Generated by Django 4.2 on 2023-05-18 06:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("theatre", "0021_alter_screen_show_times"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="screen",
            name="show_times",
        ),
        migrations.AddField(
            model_name="screen",
            name="show_times",
            field=models.ManyToManyField(to="theatre.show_time"),
        ),
    ]
