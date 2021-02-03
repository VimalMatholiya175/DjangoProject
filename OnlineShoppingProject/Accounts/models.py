from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobileNo=models.IntegerField()
    creditCardInfo=models.CharField(max_length=20)
    address=models.CharField(max_length=50)