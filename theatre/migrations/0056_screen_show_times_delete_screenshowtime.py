# Generated by Django 4.2 on 2023-06-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0055_remove_screen_show_times_screenshowtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='show_times',
            field=models.ManyToManyField(to='theatre.show_time'),
        ),
        migrations.DeleteModel(
            name='ScreenShowTime',
        ),
    ]