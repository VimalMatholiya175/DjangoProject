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
	
	data={'allProducts':allProducts,'categories':categories,'specialProducts':otherSpecialProducts,'activeProduct':activeProduct}

	return render(request,'index.html',data)


def addToCart(request):

	if not request.user.is_authenticated:
		return redirect('/')

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

def changeQty(request):

	if not request.user.is_authenticated:
		return redirect('/')

	productId=request.GET.get('id',None)

	op=request.GET.get('op',None)

	if productId is None or op is None:
		return redirect('/')

	product=Product.objects.get(id=productId)

	cart=Cart.objects.filter(product=product,user=request.user)

	if cart:
		if op=='minus':
			cart[0].quantity-=1
		else:
			cart[0].quantity+=1

		cart[0].save()


	return redirect('/viewCart')


def viewCart(request):

	if not request.user.is_authenticated:
		return redirect('/')

	carts=Cart.objects.filter(user=request.user)
	
	products=[]

	if carts:
		for cart in carts:	
			product=Product.objects.get(id=cart.product.id)
			quantity=cart.quantity
			if quantity :
				products.append((product,quantity))

	data={'products':products}

	return render(request,'cart.html',data)

		
def removeFromCart(request):

	productId=request.GET.get('id',None)

	if not request.user.is_authenticated or not productId:
		return redirect('/')

	product=Product.objects.get(id=productId)
	cart=Cart.objects.filter(product=product,user=request.user.id)
	cart[0].delete()

	return redirect('/viewCart')