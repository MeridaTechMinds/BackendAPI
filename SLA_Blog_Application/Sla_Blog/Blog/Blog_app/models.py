from django.db import models

# Create your models here.

from datetime import datetime
from django.core.exceptions import ValidationError

def validate_image_size(value):
    max_size = 5 * 1024 * 1024  # 5 MB
    if value.size > max_size:
        raise ValidationError('Maximum allowed size is 5 MB.')

class Blog(models.Model):
    slug=models.CharField(max_length=20,null=False,blank=False)
    Main_Title = models.CharField(max_length=200,null=False,blank=False)
    Sub_Title=models.CharField(max_length=200,null=True,blank=True)
    Category=models.CharField(max_length=100,null=False,blank=False)
    Points_Heading=models.CharField(max_length=100,null=True,blank=True)
    Paragraph1 = models.TextField(max_length=1500,null=False,blank=False)
    Paragraph2 = models.TextField(max_length=1500,null=True,blank=True)
    Highlight=models.CharField(max_length=1000,null=True,blank=True)
    img=models.ImageField(upload_to='images/',validators=[validate_image_size],default="images",null=False,blank=False)
    points = models.ManyToManyField('Points',null=True,blank=True)
    current_datetime = datetime.now()
    created_at = models.DateTimeField(default=current_datetime)
    comments=models.ManyToManyField("Comments",blank=True)

    def __str__(self):
        return self.Main_Title
    
class Points(models.Model):
    point=models.CharField(max_length=500)
    
    def __str__(self):

        return self.point
    
class Comments(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    comment=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.comment

class contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    interested=models.CharField(max_length=500)
    message=models.TextField(blank=True)


class Apointment(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    subjects=models.CharField(max_length=500)
    message=models.TextField(blank=True)

class Job_Portal(models.Model):
    Title=models.CharField(max_length=100)
    Experience=models.IntegerField()
    Job_Discription=models.TextField(max_length=1000)
    points=models.ManyToManyField("job_points")
    def __str__(self):
        return self.Title
    
class job_points(models.Model):
    point=models.CharField(max_length=500)
    

   
class Details(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=13)
    resume=models.FileField(upload_to="resume/")
    Message=models.TextField(max_length=1000)
    title=models.CharField(max_length=100)

    

class Enquiry_model(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=13)



class Instructor_model(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=13)
    skill=models.CharField(max_length=500)
    experience=models.CharField(max_length=20)

class Get_in_Touch(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=13)
    subject=models.CharField(max_length=500)





class contact_details(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    state=models.CharField(max_length=500)
