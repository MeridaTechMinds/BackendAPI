# Generated by Django 5.0.1 on 2024-02-03 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0013_alter_registration_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={},
        ),
        migrations.AlterField(
            model_name='registration',
            name='created_at',
            field=models.CharField(default='2024-02-03 10:02', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.CharField(default='2024-02-03 10:02:31 AM', max_length=50),
        ),
    ]
