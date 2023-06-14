# Generated by Django 4.2 on 2023-06-14 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0054_admin_sale_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screen',
            name='show_times',
        ),
        migrations.CreateModel(
            name='ScreenShowTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theatre.screen')),
                ('show_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theatre.show_time')),
            ],
        ),
    ]