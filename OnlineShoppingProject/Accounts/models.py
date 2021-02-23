from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobileNo=models.IntegerField()
    address=models.CharField(max_length=50)
