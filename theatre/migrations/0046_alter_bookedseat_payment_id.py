# Generated by Django 4.2 on 2023-06-05 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0045_bookedseat_payment_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedseat',
            name='payment_id',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
