from django.db import models

# Create your models here.
from django.db import models
from django.shortcuts import HttpResponse
from .utils import fetch_api_data

class PropertyModel(models.Model):
    def get_states():
        api_url = "http://api.nightlights.io/districts"
        api_data = fetch_api_data(api_url)
        state = []
        for i in api_data["regions"]:
            if not state or i['state_name'] != state[-1][1]:
                state.append((i['state_name'],i['state_name']))
        return state
    cc=[("Formland","Formland"),
        ("Plot","Plot"),
        ("Resort","Resort"),
        ("Buildings","Buildings")]
    category=models.CharField(max_length=500,blank=False,null=False,choices=cc)
    total_area=models.CharField(max_length=500,blank=True,null=True)
    csc=[("Apartment","Apartment"),
        ("House","House"),
        ("Commercial","Commercial"),
        ("Villas","Villas")]
    sub_category=models.CharField(max_length=500,blank=True,null=True,choices=csc)
    images = models.ManyToManyField("image_model",blank=False,null=False)
    price=models.IntegerField(blank=True,null=True)
    cdf=[("East","East"),
        ("West","West"),
        ("North","North"),
        ("South","South")]
    door_facing=models.CharField(max_length=20,blank=True,null=True,choices=cdf)
    property_id=models.CharField(max_length=20,blank=False,null=False,unique=True)
    address_line1=models.CharField(max_length=500,blank=False,null=False)
    address_line2=models.CharField(max_length=500,blank=True,null=True)
    cs=get_states()
    state = models.CharField(max_length=500,blank=False,null=False,choices=cs)
    def get_dist():
        api_url = "http://api.nightlights.io/districts"
        api_data = fetch_api_data(api_url)
        dict = []
        for i in api_data["regions"]:
            # if i['state_name']=="Andhra Pradesh":
                dict.append((i['district_name'],i['district_name']))
        return dict
    
    chd=get_dist()
    District=models.CharField(max_length=500,blank=False,null=False,choices=chd)
    pincode=models.IntegerField(blank=False,null=False)
    description=models.TextField(blank=True,null=True)

class image_model(models.Model):
    image=models.ImageField(upload_to='images/',blank=True,null=True)


class contact(models.Model):
    name=models.CharField(max_length=500,blank=False,null=False)
    email=models.EmailField(blank=False,null=False)
    message=models.TextField()

