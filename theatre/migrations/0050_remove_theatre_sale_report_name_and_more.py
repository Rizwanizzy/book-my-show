# Generated by Django 4.2 on 2023-06-05 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_userprofile_profile_image"),
        ("theatre", "0049_remove_theatre_sale_report_theatre_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="theatre_sale_report",
            name="name",
        ),
        migrations.AddField(
            model_name="theatre_sale_report",
            name="theatre",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.userprofile",
            ),
        ),
    ]
