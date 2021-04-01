from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
# Create your models here.


RAM_CHOICES=( ('None',None),('2GB','2GB'),('3GB','3GB'),
             ('4GB','4GB'),('6GB','6GB'),('8GB','8GB'),
             ('12Gb','12GB'),('16GB','16GB'),('32GB','32GB') )

STORAGE_CHOICES=( ('None',None),('16GB','16GB'),('32GB','32GB'),
                 ('64GB','64GB'),('128GB','128GB'),('256GB','256GB'),
                 ('512GB','512GB'),('1TB','1TB') )

COLOR_CHOICES=(('Black','Black'),('Red','Red'),('White','White'),
               ('Blue','Blue'),('Silver','Silver'))


class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="images/categories")

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=300)
    price=models.IntegerField()
    image=models.ImageField(upload_to="images/products")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default='All Category')
    companyName=models.CharField(max_length=50)
    quantity=models.IntegerField(default=10)
    ram=models.CharField(max_length=5,choices=RAM_CHOICES,default=None)
    storage=models.CharField(max_length=5,choices=STORAGE_CHOICES,default=None)
    color=models.CharField(max_length=6,choices=COLOR_CHOICES,default='Black')
    desc=models.TextField(max_length=800)
    discount=models.IntegerField(default=0)
    specialOffer=models.BooleanField(default=False)
    specialOfferDesc=models.TextField(max_length=300,default='No Special Offer')
    returnPolicy=models.TextField(max_length=200,default='1 year manufacturer warranty for device and 6 months manufacturer warranty for in-box accessories')
    pubDate=models.DateField()
    deliveryDays=models.IntegerField(default=4)

    def __str__(self):
        return self.name


class Cart(models.Model):

    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    
    def __str__(self):
        return self.product.name


class Order(models.Model):

    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    mobileNo=models.BigIntegerField()
    quantity=models.IntegerField()
    orderDate=models.DateField(default=datetime.today)
    address=models.TextField(max_length=250)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pincode=models.CharField(max_length=6)
    orderStatus=models.BooleanField(default=0)
    deliverDate=models.DateField(null=True,blank=True)
