# Generated by Django 5.0.1 on 2024-02-21 08:48

import datetime
import hr_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0019_alter_registration_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='created_at',
            field=models.CharField(default='2024-02-21 02:18', max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='created_date',
            field=models.DateField(default=datetime.date(2024, 2, 21)),
        ),
        migrations.AlterField(
            model_name='review',
            name='Moral_character',
            field=models.FloatField(help_text=' Moral Character out of 10', validators=[hr_app.models.validate_positive]),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.CharField(default='2024-02-21 02:18:32 PM', max_length=50),
        ),
    ]