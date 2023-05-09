# Generated by Django 4.2 on 2023-05-09 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0005_alter_movies_image'),
        ('theatre', '0003_theatre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theatre',
            name='movies',
        ),
        migrations.RemoveField(
            model_name='theatre',
            name='price1',
        ),
        migrations.RemoveField(
            model_name='theatre',
            name='price2',
        ),
        migrations.RemoveField(
            model_name='theatre',
            name='price3',
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price1', models.IntegerField()),
                ('price2', models.IntegerField()),
                ('price3', models.IntegerField()),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.movies')),
                ('theatre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='theatre.theatre')),
            ],
        ),
    ]
