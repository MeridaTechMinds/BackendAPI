# Generated by Django 5.0.1 on 2024-01-31 11:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0008_alter_registration_options_alter_review_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['user_name']},
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 31, 17, 2, 12, 600665)),
        ),
    ]