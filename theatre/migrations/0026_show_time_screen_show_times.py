# Generated by Django 4.2 on 2023-05-18 06:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("theatre", "0025_remove_screen_show_times_delete_show_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="Show_Time",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name="screen",
            name="show_times",
            field=models.ManyToManyField(to="theatre.show_time"),
        ),
    ]
