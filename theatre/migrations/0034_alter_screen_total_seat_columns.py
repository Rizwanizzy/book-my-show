# Generated by Django 4.2 on 2023-05-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0033_screen_total_seat_columns_screen_total_seat_rows_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='total_seat_columns',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
