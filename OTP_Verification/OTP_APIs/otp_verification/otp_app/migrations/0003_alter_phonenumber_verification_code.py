# Generated by Django 4.2.6 on 2024-01-01 05:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("otp_app", "0002_phonenumber_delete_otpverification"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phonenumber",
            name="verification_code",
            field=models.CharField(default="0%", max_length=6),
        ),
    ]
