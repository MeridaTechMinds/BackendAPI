# Generated by Django 5.0.1 on 2024-03-01 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0033_remove_review_last_modified_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_date',
            field=models.DateField(default=datetime.date(2024, 3, 1)),
        ),
        migrations.AlterField(
            model_name='registration',
            name='created_at',
            field=models.CharField(default='2024-03-01 10:55', max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='created_date',
            field=models.DateField(default=datetime.date(2024, 3, 1)),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.CharField(default='2024-03-01 10:55:54 PM', max_length=50),
        ),
    ]