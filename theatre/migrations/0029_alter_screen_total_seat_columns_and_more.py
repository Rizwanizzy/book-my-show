# Generated by Django 4.2 on 2023-05-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0028_alter_screen_total_seat_columns_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='total_seat_columns',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='screen',
            name='total_seat_rows',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
