# Generated by Django 3.0.5 on 2025-07-05 12:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0003_donor_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ] 