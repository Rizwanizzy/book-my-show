# Generated by Django 4.2 on 2023-05-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0012_alter_screen_price2_alter_screen_price3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='price2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='screen',
            name='price3',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]