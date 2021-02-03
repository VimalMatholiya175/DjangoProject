from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Customer
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid username/password')
            return redirect('/accounts/login')
    
    else:
        
        return render(request,'login.html')

def register(request):
    if request.method=='POST':

        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['confirmpassword']
        mobileno=request.POST['mobileno']
        creditcard=request.POST['creditcard']
        address=request.POST['address']

        if password==cpassword:

            if User.objects.filter(username=username).exists():    
                messages.info(request,'Username is already taken')
                return redirect('/accounts/register')
            
            elif User.objects.filter(email=email).exists():    
                messages.info(request,'Email is already taken')
                return redirect('/accounts/register')

            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                customer=Customer(user=user,mobileNo=mobileno,address=address,creditCardInfo=creditcard)
                customer.save()
                return redirect('/')
        
        else:
            messages.info(request,'Password doesn\'t match')
            return redirect('/accounts/register')
    else:
        
        return render(request,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')