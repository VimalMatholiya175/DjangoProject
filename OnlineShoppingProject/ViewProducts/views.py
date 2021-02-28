from django.shortcuts import render,redirect

from ShoppingApp.models import Product,Category
# Create your views here.

def viewDetails(request):

	id=request.GET.get('id',None)
	if id==None:
		return redirect('/')

	product=Product.objects.filter(id=id)
	return render(request,'viewDetails.html',{'product':product[0]})

def displayCategory(request):

	selectedCategory=request.GET.get('cat',None)
	if selectedCategory==None:
		return redirect('/')

	categories=Category.objects.all()
	category=Category.objects.get(name=selectedCategory)
	allProducts=[]
	products=Product.objects.filter(category=category)
	allProducts.append(products)

	colors=set()
	sizes=set()
	companies=set()

	for product in products:
		colors.add(product.get_color_display())
		if product.get_ram_display()!='None':
			sizes.add((product.get_ram_display(),product.get_storage_display()))
		companies.add(product.companyName)
	
	data={'allProducts':allProducts,'categories':categories,'colors':colors,'sizes':sizes,'companies':companies,'category':selectedCategory,'message':None}
	return render(request,'displayCategory.html',data)

def xfilter(request):

	price=request.GET.get('price',None)
	size=request.GET.get('size',None)
	company=request.GET.get('company',None)
	color=request.GET.get('color',None)
	selectedCategory=request.GET.get('cat',None)
	
	if selectedCategory==None:
		return redirect('/')

	if price==None or company==None or color==None:
		return redirect('/viewProducts/displayCategory?cat='+selectedCategory)


	categories=Category.objects.all()
	category=Category.objects.get(name=selectedCategory)

	products=Product.objects.filter(category=category)

	colors=set()
	sizes=set()
	companies=set()

	for product in products:
		colors.add(product.get_color_display())
		if product.get_ram_display()!='None':
			sizes.add((product.get_ram_display(),product.get_storage_display()))
		companies.add(product.companyName)

	allProducts=[] 
	
	if size != None:
		ram,storage=size.split(' | ')
		if price=='lth':
			products=Product.objects.order_by('price').filter(category=category,companyName=company,color=color,ram=ram,storage=storage)
		else:
			products=Product.objects.order_by('-price').filter(category=category,companyName=company,color=color,ram=ram,storage=storage)
	else:
		if price=='lth':
			products=Product.objects.order_by('price').filter(category=category,companyName=company,color=color)
		else:
			products=Product.objects.order_by('-price').filter(category=category,companyName=company,color=color)

	allProducts.append(products)

	if len(products)==0 or len(allProducts):
		message='No Matches were found...'
	else:
		message=None
	
	data={'allProducts':allProducts,'categories':categories,'colors':colors,'sizes':sizes,'companies':companies,'category':selectedCategory,'message':message}

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
					
				if count==3:
					matchedProducts.append(product)

		if len(matchedProducts)==0:
			continue


		matchedCategories.append(matchedProducts)

	data={'matchedCategories':matchedCategories,'keyword':keyword}
	return render(request,'search.html',data)
