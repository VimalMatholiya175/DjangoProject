from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse

from .models import Category,Product,Cart
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
	
	data={'allProducts':allProducts,'categories':categories,'specialProducts':otherSpecialProducts,'activeProduct':activeProduct,'forRam':['Mobile','Laptop']}

	return render(request,'index.html',data)


def addToCart(request):

	productId=request.GET.get('id',None)
	if not productId:
		return redirect('/')

	product=Product.objects.get(id=productId)

	if productId is None:
		return redirect('/')

	cart=Cart.objects.filter(product=product,user=request.user)

	if cart:
		cart[0].quantity+=1
		cart[0].save()
	else:
		cart=Cart(product=product,user=request.user,quantity=1)
		cart.save()

	return redirect('/viewProducts/viewDetails?id='+productId)



		



		

