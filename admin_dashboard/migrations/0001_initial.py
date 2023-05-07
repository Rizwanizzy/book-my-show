# Generated by Django 4.2 on 2023-05-06 04:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='All_Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='movie_images')),
                ('release_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('trailer', models.URLField(max_length=300)),
                ('runtime', models.DurationField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.all_comments')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.all_languages')),
            ],
        ),
    ]
