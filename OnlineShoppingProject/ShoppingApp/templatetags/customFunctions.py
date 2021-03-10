from django import template

register = template.Library()

@register.filter(name='actualPrice')
def actualPrice(price,discount):
	actualPrice=price - (discount/100)*price
	return int(actualPrice)


@register.filter(name='replaceNewLines')
def replaceNewLines(desc):
	desc="• "+desc
	desc=desc.replace('\n','\n• ')
	return desc


@register.filter(name='hasRam')
def hasRam(category):
	if category.name in ['Mobile','Laptop']:
		return True

	return False
