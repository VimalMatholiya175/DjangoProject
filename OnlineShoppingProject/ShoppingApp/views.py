from django.shortcuts import render

from .models import Product
# Create your views here.

def home(request):
	prods=Product.objects.values()
	categories={item['category'] for item in prods}
	category=request.GET.get('category',None)

	if category==None:
		allProducts=[]
		for cat in categories:
			product=Product.objects.filter(category=cat)
			allProducts.append(product)
	else:
		allProducts=[]
		categories.remove(category)
		product=Product.objects.filter(category=category)
		allProducts.append(product)

	return render(request,'index.html',{'allProducts':allProducts,'categories':categories,'scategory':category})

def viewProduct(request):

	id=request.GET['id']
	product=Product.objects.filter(id=id)
	
	
	return render(request,'viewProduct.html',{'product':product[0]})

