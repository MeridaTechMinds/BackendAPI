from django.db import models

# Create your models here.

from datetime import datetime
from django.utils import timezone

class registration(models.Model):
    Name=models.CharField(max_length=100,null=False,blank=False)
    Primary_contact=models.CharField(max_length=13,null=False,blank=False)
    Secondary_contact=models.CharField(max_length=13,null=True,blank=True)
    Location=models.CharField(max_length=1000,default=" ",null=False,blank=False)
    Email_Id=models.EmailField(null=False,blank=False)
    Current_CTC=models.CharField(max_length=50,null=False,blank=False)
    Expected_CTC=models.CharField(max_length=50,null=False,blank=False)
    Notice_Period=models.CharField(max_length=50,null=False,blank=False)
    Current_designation=models.CharField(max_length=100,default=' ',null=False,blank=False)
    Applied_designation=models.CharField(max_length=100,default=' ',null=False,blank=False)
    experience=models.CharField(max_length=100,null=True,blank=True)
    General_Skills=models.TextField(null=False,blank=False)
    Technical_Skills=models.TextField(null=False,blank=False)
    Soft_Skills=models.TextField(null=False,blank=False)
    Job_portal_source=models.CharField(max_length=100,null=False,blank=False)
    Contacted_by=models.CharField(max_length=100,null=False,blank=False)
    Contacted_person_no=models.CharField(max_length=100,null=True,blank=True,default=" ")
    current_datetime = timezone.localtime(timezone.now())
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %I:%M')
    created_at = models.CharField(max_length=50,default=formatted_datetime[0:17])
    today = timezone.localdate()
    from datetime import date

    created_date = models.DateField(default=date.today)
    
    

    def __str__(self):
        return self.Name
    

from django.core.exceptions import ValidationError
def validate_positive(value):
    if value <= 0:
        raise ValidationError(
            '%(value)s is not a positive number',
            params={'value': value},
        )
    
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.db.models.signals import pre_save


def get_reviewed_by(username):
    return username


class Review(models.Model):
    
    user_name=models.OneToOneField(registration,on_delete=models.CASCADE)
    Moral_character=models.FloatField( validators=[validate_positive],
                                        help_text=" Moral Character out of 10")
    punctuality=models.FloatField(validators=[validate_positive],
                                        help_text=" Punctuality out of 10")
    health=models.FloatField(validators=[validate_positive],
                                        help_text=" Health out of 10")
    behaviour=models.FloatField(validators=[validate_positive],
                                        help_text=" Behaviour out of 10",null=True)
    attitude=models.FloatField(validators=[validate_positive],
                                        help_text=" marks out of 10")
    Career_goals=models.CharField(max_length=100)
    understanding_level=models.FloatField(validators=[validate_positive],
                                        help_text=" Understanding level out of 10")
    possitive_attitude_and_mind=models.FloatField( validators=[validate_positive],
                                        help_text=" Possitive attitude and mind out of 10",null=True)
    executive=models.FloatField(validators=[validate_positive],
                                        help_text=" Executive out of 10",null=True)
    responsibility=models.FloatField( validators=[validate_positive],
                                        help_text=" Responsibility out of 10")
    response_ability=models.FloatField( validators=[validate_positive],
                                        help_text=" Response Ability out of 10")
    team_handling=models.IntegerField( validators=[validate_positive],
                                        help_text=" Team handling out of 10")
    planing=models.FloatField( validators=[validate_positive],
                                        help_text=" Planing out of 10")
    communicate_ability=models.FloatField( validators=[validate_positive],
                                        help_text=" Communicate Ability out of 10")
    passion=models.CharField(max_length=100)
    confidence=models.FloatField( validators=[validate_positive],
                                        help_text=" Confidence out of 10")
    profissional_background=models.CharField(max_length=100)
    work_experience=models.FloatField( validators=[validate_positive],
                                        help_text=" Work Experience Max 25 Years")
    knowledge_level=models.FloatField( validators=[validate_positive],
                                        help_text=" Knowledge Level out of 10")
    english_skils=models.FloatField( validators=[validate_positive],
                                        help_text="English Skils out of 10")
    other_languages=models.CharField(max_length=1000,default=' ')
    c=[
        (" "," "),
        ("yes","yes"),
        ("no","no")
       ]
    consider_to_client=models.CharField(max_length=10,default=' ',choices=c)
    Internal_hiring=models.CharField(max_length=10,default=' ',choices=c)
    reject=models.CharField(max_length=10,default=' ',choices=c)
    current_datetime = timezone.localtime(timezone.now())
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %I:%M:%S %p')
    created_at = models.CharField(max_length=50,default=formatted_datetime)
    today = timezone.localdate()
    # created_date = models.DateField(default=today)
    remarks=models.TextField()
    ReviewedBy = models.CharField(max_length=100, default="")
    @receiver(user_logged_in)
    def send_login_notification(sender, request, user, **kwargs):
        if user.is_superuser:
            logedin_user = get_reviewed_by(user.username)
        else:
            # For staff users, we can simply use their username
            logedin_user = get_reviewed_by(user.username)
        Review._meta.get_field('ReviewedBy').default = logedin_user

    class Meta:
        ordering = ['user_name']
    def __str__(self):
        return f"{self.user_name.Name}"
    

    




    
