from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=300)
    price=models.IntegerField()
    discount=models.IntegerField(default=0)
    category=models.CharField(max_length=50)
    desc=models.TextField(max_length=800)
    # outOfStock=models.BooleanField(default=False)
    quantity=models.IntegerField(default=0)
    specialOffer=models.BooleanField(default=False)
    image=models.ImageField(upload_to="images/products")
    pubDate=models.DateField()


    def __str__(self):
        return self.name