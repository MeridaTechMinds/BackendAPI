# Generated by Django 5.0.1 on 2024-02-15 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0015_alter_registration_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='created_date',
            field=models.DateField(default=datetime.date(2024, 2, 15)),
        ),
        migrations.AlterField(
            model_name='registration',
            name='created_at',
            field=models.CharField(default='2024-02-15 04:08', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.CharField(default='2024-02-15 04:08:07 PM', max_length=50),
        ),
    ]
