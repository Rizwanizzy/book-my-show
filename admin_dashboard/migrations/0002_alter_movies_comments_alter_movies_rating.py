# Generated by Django 4.2 on 2023-05-06 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("admin_dashboard", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movies",
            name="comments",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="admin_dashboard.all_comments",
            ),
        ),
        migrations.AlterField(
            model_name="movies",
            name="rating",
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
    ]
