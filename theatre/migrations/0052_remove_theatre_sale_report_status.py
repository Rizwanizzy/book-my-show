# Generated by Django 4.2 on 2023-06-05 14:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("theatre", "0051_remove_theatre_sale_report_theatre_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="theatre_sale_report",
            name="status",
        ),
    ]
