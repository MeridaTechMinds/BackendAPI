# Generated by Django 5.0.1 on 2024-02-28 16:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0029_remove_review_reviewedby_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='created_at',
            field=models.CharField(default='2024-02-28 10:23', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.CharField(default='2024-02-28 10:23:23 PM', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewedby',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
