# Generated by Django 3.2.9 on 2023-05-12 06:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_dashboard", "0005_alter_movies_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movies",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="movies",
            name="genre",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="movies",
            name="runtime",
            field=models.DurationField(blank=True),
        ),
        migrations.AlterField(
            model_name="movies",
            name="trailer",
            field=models.URLField(blank=True, max_length=300),
        ),
    ]
