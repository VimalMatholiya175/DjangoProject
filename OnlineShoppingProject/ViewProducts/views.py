from django.shortcuts import render,redirect

from ShoppingApp.models import Product,Category,Cart
# Create your views here.


def productDetails(request,id):

	if id==None:
		return redirect('/')

	product=Product.objects.get(id=id)

	products=Product.objects.filter(name=product.name)

	sProducts=set()
	for prod in products:
		sProducts.add((prod.id,prod.get_color_display(),prod.get_ram_display(),prod.get_storage_display()))

	data={'product':product,'sProducts':sProducts}
	return render(request,'productDetails.html', data)



def afilter(request,selectedCategory):

	price=request.GET.get('price')
	company=request.GET.get('company')
	
	if not selectedCategory:
		return redirect('/')

	allProducts=[]

	category=Category.objects.get(name=selectedCategory)
	products=Product.objects.filter(category=category)
	companies=set()
	for product in products:
		companies.add(product.companyName)

	if price and company:
		if price=='lth':
			products=Product.objects.order_by('price').filter(category=category,companyName=company)
		else:
			products=Product.objects.order_by('-price').filter(category=category,companyName=company)

	elif not price and company:
		products=Product.objects.filter(category=category,companyName=company)
	
	else:
		if price == 'lth':
			products=Product.objects.order_by('price').filter(category=category)
		else:
			products=Product.objects.order_by('-price').filter(category=category)

	allProducts.append(products)
	
	data={'allProducts':allProducts,'category':selectedCategory,'companies':companies}

	return render(request,'afilter.html',data)



def search(request):
	keyword=request.GET.get('keyword',None)
	if keyword==None:
		return redirect('/')

	oKeyword=keyword
	if keyword[len(keyword)-1]=='s':
		keyword=keyword[:len(keyword)-1]
	
	keywords=keyword.split(' ')
	
	matchedCategories=[]
	categories=Category.objects.all()

	for cat in categories:

		products=Product.objects.filter(category=cat)
		matchedProducts=[]
		for product in products:
			if keyword==product.name.lower() or keyword == product.companyName.lower() or keyword == product.category.name.lower():
				matchedProducts.append(product)
			elif len(keywords) == 2 and keywords[0] == product.companyName.lower() and  keywords[1]== product.category.name.lower():
				matchedProducts.append(product)
			elif len(keywords) >= 1:
				count=0
				for word in keywords:
					if word in product.name.lower():
						count+=1
				if count>=5:
					matchedProducts.append(product)
				elif count>=4:
					matchedProducts.append(product)
				elif count>=3:
					matchedProducts.append(product)
				elif count>=2:
					matchedProducts.append(product)
				
		if len(matchedProducts)==0:
			continue

		matchedCategories.append(matchedProducts)

	data={'matchedCategories':matchedCategories,'keyword':oKeyword}
	return render(request,'search.html',data)
