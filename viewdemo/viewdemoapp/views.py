from django.shortcuts import render

# Create your views here.

def index(request):

	if request.method=='POST':

		name=request.POST['name']
		return render(request,'index.html',{'name': name,'bool': True})

	else:

		return render(request,'index.html')