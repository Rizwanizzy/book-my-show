# Generated by Django 4.2 on 2023-05-18 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0022_remove_screen_show_times_screen_show_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='show_times',
            field=models.ManyToManyField(null=True, to='theatre.show_time'),
        ),
    ]
