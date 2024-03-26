from django.db import models

# Create your models here.
class PhoneNumber(models.Model):
    name=models.CharField(max_length=100,unique=False,null=False,default="name")
    phone_number = models.CharField(max_length=15, unique=True)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6)
    count_no=models.IntegerField(default=0)
    offer=models.CharField(max_length=100,default="0%")