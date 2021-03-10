from django.shortcuts import render,redirect

from ShoppingApp.models import Product,Category,Cart
# Create your views here.

def viewDetails(request):

	id=request.GET.get('id',None)
	if id==None:
		return redirect('/')

	product=Product.objects.get(id=id)
	
	quantity=0

	if request.user.is_authenticated :
		cart=Cart.objects.filter(product=product,user=request.user)
		if cart :
			quantity=cart[0].quantity

	data={'product':product,'quantity':quantity}
	return render(request,'viewDetails.html', data)


def displayCategory(request):

	selectedCategory=request.GET.get('cat',None)
	if selectedCategory==None:
		return redirect('/')

	categories=Category.objects.all()
	category=Category.objects.get(name=selectedCategory)
	allProducts=[]
	products=Product.objects.filter(category=category)
	allProducts.append(products)

	companies=set()

	for product in products:
		companies.add(product.companyName)
	
	data={'allProducts':allProducts,'categories':categories,'companies':companies,'category':selectedCategory}
	return render(request,'displayCategory.html',data)


def xfilter(request):

	price=request.GET.get('price',None)
	company=request.GET.get('company',None)
	selectedCategory=request.GET.get('cat',None)
	
	if selectedCategory==None:
		return redirect('/')

	if price==None and company==None:
		return redirect('/viewProducts/displayCategory?cat='+selectedCategory)

	categories=Category.objects.all()
	category=Category.objects.get(name=selectedCategory)
	products=Product.objects.filter(category=category)

	companies=set()
	for product in products:
		companies.add(product.companyName)

	allProducts=[] 
	
	if price != None and company != None:
		if price=='lth':
			products=Product.objects.order_by('price').filter(category=category,companyName=company)
		else:
			products=Product.objects.order_by('-price').filter(category=category,companyName=company)

	elif price==None and company!=None:
		products=Product.objects.filter(category=category,companyName=company)
	
	else:
		if price == 'lth':
			products=Product.objects.order_by('price').filter(category=category)
		else:
			products=Product.objects.order_by('price').filter(category=category)

	allProducts.append(products)
	
	data={'allProducts':allProducts,'categories':categories,'companies':companies,'category':selectedCategory}

	return render(request,'displayCategory.html',data)


def search(request):
	keyword=request.GET.get('keyword',None)
	if keyword==None:
		return redirect('/')
	
	keywords=keyword.split(' ')
	
	matchedCategories=[]
	categories=Category.objects.all()

	for cat in categories:

		products=Product.objects.filter(category=cat)
		matchedProducts=[]
		for product in products:
			if  keyword in product.companyName.lower() or keyword in product.category.name.lower() or keyword in product.category.name.lower()+'s':
				matchedProducts.append(product)
			elif len(keywords) == 2 and keywords[0] in product.companyName.lower() and ( keywords[1] in product.category.name.lower() or keywords[1] in product.category.name.lower()+'s' ):
				matchedProducts.append(product)
			elif len(keywords) >= 2:
				count=0
				for word in keywords:
					if word in product.name.lower():
						count+=1
					
				if count>=3:
					matchedProducts.append(product)
				elif count>=2:
					matchedProducts.append(product)

		if len(matchedProducts)==0:
			continue

		matchedCategories.append(matchedProducts)

	data={'matchedCategories':matchedCategories,'keyword':keyword}
	return render(request,'search.html',data)
