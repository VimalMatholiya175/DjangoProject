from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobileNo=models.BigIntegerField()
    city=models.CharField(max_length=20,null=True,blank=True)
    state=models.CharField(max_length=20,null=True,blank=True)
    pincode=models.CharField(max_length=6,null=True,blank=True)
    address=models.TextField(max_length=250,null=True,blank=True)
