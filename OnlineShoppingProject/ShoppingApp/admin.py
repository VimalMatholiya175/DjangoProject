from django.contrib import admin
from .models import Category,Product,Order
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','color','quantity','specialOffer']
    list_editable=['quantity','specialOffer']

class AdminOrder(admin.ModelAdmin):
    list_display=['product','name','quantity','orderDate','orderStatus','deliverDate']
    list_editable=['orderStatus','deliverDate']


admin.site.register(Product,AdminProduct)
admin.site.register(Category)
# admin.site.register(Cart)
admin.site.register(Order,AdminOrder)