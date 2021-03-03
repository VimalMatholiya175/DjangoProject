from django.shortcuts import render,redirect
from django.contrib import messages
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
	
	data={'allProducts':allProducts,'categories':categories,'specialProducts':otherSpecialProducts,'activeProduct':activeProduct,'forRam':['Mobile','Laptop']}

	return render(request,'index.html',data)

def addToCart(request):

	if not request.user.is_authenticated :

		messages.info(request,'Login first...')
		return redirect('/accounts/login')

	productId=request.GET.get('id',None)

	if productId is None:
		return redirect('/')

	cart=request.session.get('cart')
	if cart :
		quantity=cart.get(productId)
		if quantity:
			cart[productId]=quantity+1
		else:
			cart[productId]=1
	else:
		cart={productId:1}
		
	request.session['cart']=cart
	# print(cart)
	return redirect('/viewProducts/viewDetails?id='+productId)

def iQuantity(request):
	productId=request.GET.get('id',None)

	if productId is None:
		return redirect('/')

	cart=request.session.get('cart')
	cart[productId]+=1
	request.session['cart']=cart
	return redirect('/viewProducts/viewDetails?id='+productId)

def dQuantity(request):
	productId=request.GET.get('id',None)

	if productId is None:
		return redirect('/')

	cart=request.session.get('cart')
	cart[productId]-=1
	request.session['cart']=cart
	return redirect('/viewProducts/viewDetails?id='+productId)