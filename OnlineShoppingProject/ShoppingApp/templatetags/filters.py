from django import template
from ShoppingApp.models import Cart,Category

register = template.Library()


@register.filter(name='actualPrice')
def actualPrice(product):
	actualPrice=product.price - (product.discount/100)*product.price
	return int(actualPrice)


@register.filter(name='replaceNewLines')
def replaceNewLines(desc):
	desc="• "+desc
	desc=desc.replace('\n','\n• ')
	return desc


@register.filter(name='isInCart')
def isInCart(product,user):
	cart=Cart.objects.filter(product=product,user=user)
	if cart :
		return True
	return False


@register.filter(name='hasRam')
def hasRam(category):	
	if category.name in ['Mobile','Laptop']:
		return True
	return False


@register.filter(name='amountToPay')
def amountToPay(products):	
	actualAmount=0
	for product,quantity in products:
		actualAmount+=actualPrice(product)*quantity
	return actualAmount


@register.filter(name='totalSavings')
def totalSavings(products):
	actualAmount=totalAmount=0
	for product,quantity in products:
		actualAmount+=actualPrice(product)*quantity
		totalAmount+=product.price*quantity
	return totalAmount-actualAmount


@register.filter(name='deliveryDays')
def deliverydays(products):
	days=0
	for product,quantity in products:
		if product.deliveryDays > days:
			days=product.deliveryDays
	return days


@register.filter(name='totalProducts')
def totalProducts(user):
	carts=Cart.objects.filter(user=user)
	totalProducts = 0
	for cart in carts:
		totalProducts+=cart.quantity
	return totalProducts


@register.filter(name='allCategories')
def allCategories(user):
	categories=Category.objects.all()
	return categories