# Generated by Django 3.2.5 on 2021-08-20 12:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreaction',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
