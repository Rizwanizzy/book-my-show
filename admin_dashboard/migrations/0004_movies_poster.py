# Generated by Django 4.2 on 2023-05-08 09:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_dashboard", "0003_alter_movies_comments_alter_movies_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="movies",
            name="poster",
            field=models.ImageField(blank=True, upload_to="movie_images"),
        ),
    ]
