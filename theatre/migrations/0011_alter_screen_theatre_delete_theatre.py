# Generated by Django 4.2 on 2023-05-10 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('theatre', '0010_alter_theatre_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userprofile'),
        ),
        migrations.DeleteModel(
            name='Theatre',
        ),
    ]