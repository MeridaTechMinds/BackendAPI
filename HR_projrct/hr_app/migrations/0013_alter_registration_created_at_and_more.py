# Generated by Django 5.0.1 on 2024-02-01 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0012_alter_registration_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='created_at',
            field=models.CharField(default='2024-02-01 10:20:10 AM', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.CharField(default='2024-02-01 10:20:10 AM', max_length=50),
        ),
    ]