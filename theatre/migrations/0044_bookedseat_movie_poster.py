# Generated by Django 4.2 on 2023-05-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0043_bookedseat_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedseat',
            name='movie_poster',
            field=models.ImageField(blank=True, upload_to='booked_movie_images'),
        ),
    ]
