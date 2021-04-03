from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views import View

from Accounts.models import Customer
from .models import Category,Product,Cart,Order

# Create your views here.

def home(request):

	specialProducts=Product.objects.filter(specialOffer=True)
	activeProduct=specialProducts[0]
	otherSpecialProducts=specialProducts[1:]

	allProducts=[]
	categories=Category.objects.all()
	for category in categories:
		products=Product.objects.filter(category=category)
		allProducts.append(products)
	
	data={'allProducts':allProducts,'specialProducts':otherSpecialProducts,'activeProduct':activeProduct}

	return render(request,'index.html',data)


def viewCart(request):

	carts=Cart.objects.filter(user=request.user)
	
	products=[]
	if carts:
		for cart in carts:	
			product=Product.objects.get(id=cart.product.id)
			quantity=cart.quantity
			if quantity :
				products.append((product,quantity))
			else:
				cart.delete()
	data={'products':products}

	return render(request,'cart.html',data)


def addToCart(request):

	productId=request.GET.get('id')
	if productId==None:
		return redirect('/')

	product=Product.objects.get(id=productId)
	cart=Cart.objects.filter(product=product,user=request.user)

	if cart:
		cart[0].quantity+=1
		cart[0].save()
	else:
		cart=Cart(product=product,user=request.user,quantity=1)
		cart.save()

	return redirect('/viewProducts/productDetails/'+productId)

def changeQty(request,productId,op):

	if productId is None or op is None:
		return redirect('/')

	product=Product.objects.get(id=productId)

	cart=Cart.objects.filter(product=product,user=request.user)

	if cart:
		if op=='minus':
			cart[0].quantity-=1
		else:
			if product.quantity==cart[0].quantity:
				messages.info(request,'This product is now out of stock')
				return redirect('/viewCart')
			else:
				cart[0].quantity+=1

		cart[0].save()

	return redirect('/viewCart')

		
def removeFromCart(request,productId):

	if not productId:
		return redirect('/')

	product=Product.objects.get(id=productId)
	cart=Cart.objects.filter(product=product,user=request.user)
	cart[0].delete()

	return redirect('/viewCart')



class Checkout(View):

	def get(self,request):

		productId=request.GET.get('id')
		status=request.GET.get('status')
		
		products=[]
		customer=Customer.objects.get(user_id=request.user.id)
		if productId:
			product=Product.objects.get(id=productId)
			if not product.quantity:
				return redirect('/')
			products.append((product,1))
		
		else:
			carts=Cart.objects.filter(user=request.user)
			if not carts:
				return redirect('/')
			for cart in carts:
				product=Product.objects.get(id=cart.product.id)
				products.append((product,cart.quantity))

		data={'products':products,'id':productId,'customer':customer,'status':status}
		return render(request,'checkout.html',data)

	def post(self,request):

		firstname=request.POST.get('firstname')
		lastname=request.POST.get('lastname')
		mobileNo=request.POST.get('mobileno')
		pincode=request.POST.get('pincode')
		city=request.POST.get('city')
		state=request.POST.get('state')
		address=request.POST.get('address')

		if request.POST.get('save')=='True':
			customer=Customer.objects.get(user_id=request.user.id)
			customer.pincode=pincode
			customer.mobileNo=mobileNo
			customer.city=city
			customer.state=state
			customer.address=address
			customer.save()
			request.user.first_name=firstname
			request.user.last_name=lastname
			request.user.save()

		productId=request.POST.get('id')

		if productId != 'None':
			product=Product.objects.get(id=productId)
			product.quantity-=1
			product.save()
			order=Order(product=product,user=request.user,quantity=1,name=firstname+' '+lastname,mobileNo=mobileNo,pincode=pincode,city=city,state=state,address=address)
			order.save()
	 	
		else:
			carts=Cart.objects.filter(user=request.user)
			for cart in carts:
				cart.product.quantity-=cart.quantity
				cart.product.save()
				order=Order(product=cart.product,user=cart.user,quantity=cart.quantity,name=firstname+' '+lastname,mobileNo=mobileNo,pincode=pincode,city=city,state=state,address=address)
				order.save()
				cart.delete()
		
		return redirect('/orders')



def orders(request):

	if request.method=='GET':

		orders=Order.objects.filter(user=request.user).order_by('-orderDate')

		data={'orders':orders}
		return render(request,'orders.html',data)

def cancelOrder(request,orderId):

	if orderId:
		order=Order.objects.get(id=orderId)
		order.product.quantity+=order.quantity
		order.product.save()
		order.delete()
		return redirect('/orders')
	else:
		return redirect('/')