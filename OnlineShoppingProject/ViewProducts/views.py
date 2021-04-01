from django.shortcuts import render,redirect

from ShoppingApp.models import Product,Category,Cart
# Create your views here.


def productDetails(request):

	id=request.GET.get('id',None)
	if id==None:
		return redirect('/')

	product=Product.objects.get(id=id)

	data={'product':product}
	return render(request,'productDetails.html', data)



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
			products=Product.objects.order_by('-price').filter(category=category)

	allProducts.append(products)
	
	data={'allProducts':allProducts,'categories':categories,'companies':companies,'category':selectedCategory}

	return render(request,'displayCategory.html',data)



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
