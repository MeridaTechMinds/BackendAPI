# Generated by Django 5.0.1 on 2024-02-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0027_alter_registration_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ReviewedBy',
            field=models.CharField(choices=[], default='', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='created_at',
            field=models.CharField(default='2024-02-28 05:10', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.CharField(default='2024-02-28 05:10:51 PM', max_length=50),
        ),
    ]