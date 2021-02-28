from django.db import models

# Create your models here.

RAM_CHOICES=(('None','None'),('2','2GB'),('3','3GB'),('4','4GB'),('6','6GB'),('8','8GB'),('12','12GB'),('16','16GB'),('32','32GB'))
STORAGE_CHOICES=(('None','None'),('16','16GB'),('32','32GB'),('64','64GB'),('128','128GB'),('256','256GB'),('512','512GB'),('1024','1TB'))
COLOR_CHOICES=(('black','Black'),('red','Red'),('white','White'),('blue','Blue'),('silver','Silver'))

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
    ram=models.CharField(max_length=5,choices=RAM_CHOICES,default='None')
    storage=models.CharField(max_length=5,choices=STORAGE_CHOICES,default='None')
    color=models.CharField(max_length=6,choices=COLOR_CHOICES,default='black')
    desc=models.TextField(max_length=800)
    discount=models.IntegerField(default=0)
    specialOffer=models.BooleanField(default=False)
    specialOfferDesc=models.TextField(max_length=300,default='No Special Offer')
    returnPolicy=models.TextField(max_length=200,default='1 year manufacturer warranty for device and 6 months manufacturer warranty for in-box accessories')
    pubDate=models.DateField()

    def __str__(self):
        return self.name
