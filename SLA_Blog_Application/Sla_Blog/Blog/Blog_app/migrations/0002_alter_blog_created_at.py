# Generated by Django 5.0.1 on 2024-02-03 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 3, 11, 24, 7, 58718)),
        ),
    ]
