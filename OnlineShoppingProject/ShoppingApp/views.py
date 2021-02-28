from django.shortcuts import render
from django.http import HttpResponse

from .models import Category,Product
# Create your views here.

def home(request):

	categories=Category.objects.all()

	specialProducts=Product.objects.filter(specialOffer=True)
	activeProduct=specialProducts[0]
	otherSpecialProducts=specialProducts[1:]

	allProducts=[]

	for category in categories:
		products=Product.objects.filter(category=category)
		allProducts.append(products)
	
	data={'allProducts':allProducts,'categories':categories,'specialProducts':otherSpecialProducts,'activeProduct':activeProduct}

	return render(request,'index.html',data)



