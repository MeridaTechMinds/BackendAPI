# Generated by Django 5.0.1 on 2024-01-31 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0007_registration_location_alter_review_behaviour_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ['Name']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['user_name__Name']},
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 31, 16, 49, 29, 219856)),
        ),
    ]
