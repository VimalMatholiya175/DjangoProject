from django.db import models

# Create your models here.

class book_master(models.Model):
	book_id = models.IntegerField(primary_key = True)
	book_name = models.CharField(max_length = 100)
	book_price = models.IntegerField()