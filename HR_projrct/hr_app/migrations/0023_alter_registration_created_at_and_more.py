# Generated by Django 5.0.1 on 2024-02-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0022_review_reviewedby_alter_registration_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='created_at',
            field=models.CharField(default='2024-02-28 04:35', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.CharField(default='2024-02-28 04:35:26 PM', max_length=50),
        ),
    ]