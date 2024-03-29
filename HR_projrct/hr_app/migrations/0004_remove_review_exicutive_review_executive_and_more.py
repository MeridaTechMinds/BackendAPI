# Generated by Django 5.0.1 on 2024-01-31 07:15

import datetime
import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0003_alter_registration_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='exicutive',
        ),
        migrations.AddField(
            model_name='review',
            name='executive',
            field=models.FloatField(help_text=' Executive out of 10', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='review',
            name='Internal_hiring',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default=' ', max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='Moral_character',
            field=models.FloatField(help_text=' Moral Character out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='attitude',
            field=models.FloatField(help_text=' marks out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='communicate_ability',
            field=models.FloatField(help_text=' Communicate Ability out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='confidence',
            field=models.FloatField(help_text=' Confidence out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 31, 12, 45, 0, 24788)),
        ),
        migrations.AlterField(
            model_name='review',
            name='english_skils',
            field=models.FloatField(help_text='English Skils out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='health',
            field=models.FloatField(help_text=' Health out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='knowledge_level',
            field=models.FloatField(help_text=' Knowledge Level out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='other_languages',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='planing',
            field=models.FloatField(help_text=' Planing out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='poilitness_quiteness',
            field=models.FloatField(help_text=' Poilitness and Quiteness out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='positive_mind',
            field=models.FloatField(help_text=' Positive mind out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='possitive_attitude',
            field=models.FloatField(help_text=' Possitive attitude out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='punctuality',
            field=models.FloatField(help_text=' Punctuality out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='reject',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default=' ', max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='response_ability',
            field=models.FloatField(help_text=' Response Ability out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='responsibility',
            field=models.FloatField(help_text=' Responsibility out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='understanding_level',
            field=models.FloatField(help_text=' Understanding level out of 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='work_experience',
            field=models.FloatField(help_text=' Work Experience Max 25 Years', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(25)]),
        ),
    ]
