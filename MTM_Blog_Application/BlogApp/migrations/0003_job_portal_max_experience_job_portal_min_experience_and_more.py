# Generated by Django 5.0.1 on 2024-02-19 10:11

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_alter_blog_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_portal',
            name='Max_Experience',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AddField(
            model_name='job_portal',
            name='Min_Experience',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 19, 15, 41, 18, 256998)),
        ),
        migrations.AlterField(
            model_name='job_portal',
            name='Experience',
            field=models.IntegerField(blank=True),
        ),
    ]
