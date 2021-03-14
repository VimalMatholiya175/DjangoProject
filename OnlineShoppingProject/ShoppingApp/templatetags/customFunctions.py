from django import template
from ShoppingApp.models import Cart

register = template.Library()

@register.filter(name='actualPrice')
def findActualPrice(price,discount):
	actualPrice=price - (discount/100)*price
	return int(actualPrice)


@register.filter(name='replaceNewLines')
def replaceNewLines(desc):
	desc="• "+desc
	desc=desc.replace('\n','\n• ')
	return desc


@register.filter(name='isProductInCart')
def isProductInCart(product,user):
	# if request.user.is_authenticated :
	cart=Cart.objects.filter(product=product,user=user)
	if cart :
		return True

	return False


@register.filter(name='hasRam')
def hasRam(category):
	if category.name in ['Mobile','Laptop']:
		return True

	return False


@register.filter(name='totalAmount')
def findTotalAmount(products,user):
	totalAmount=0
	for product,quantity in products:

		totalAmount+=findActualPrice(product.price,product.discount)*quantity

	return totalAmount