# Generated by Django 4.2 on 2023-05-09 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0005_alter_movies_image'),
        ('theatre', '0002_rename_is_theatre_owner_userprofile_is_theatre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('price1', models.IntegerField()),
                ('price2', models.IntegerField()),
                ('price3', models.IntegerField()),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.movies')),
                ('userprofile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='theatre.userprofile')),
            ],
        ),
    ]
