# Generated by Django 4.2.6 on 2024-01-01 06:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("otp_app", "0003_alter_phonenumber_verification_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phonenumber",
            name="phone_number",
            field=models.CharField(default="+91", max_length=15, unique=True),
        ),
    ]
