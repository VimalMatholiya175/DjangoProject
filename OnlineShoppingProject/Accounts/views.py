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
            messages.info(request,'Incorrect Username/Password')
            return redirect('login')
    
    else:
        
        return render(request,'login.html')

def register(request):
    if request.method=='POST':

        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['confirmpassword']
        mobileno=request.POST['mobileno']
        address=request.POST['address']

        if password==cpassword:

            if User.objects.filter(username=username).exists():    
                messages.info(request,'Username is already taken')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():    
                messages.info(request,'Email is already taken')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                customer=Customer(user=user,mobileNo=mobileno,address=address)
                customer.save()
                return redirect('login')
        
        else:
            messages.info(request,'Password doesn\'t match')
            return redirect('register')
    else:
        
        return render(request,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def reset(request):

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['confirmpassword']

        if User.objects.filter(username=username).exists():
            if password==cpassword:
                user=User.objects.get(username=username)
                user.set_password(password)
                user.save()
                return redirect('login')
            else:
                messages.info(request,'Password doesn\'t match')
                return redirect('reset')
        else:
            messages.info(request,'Username doesn\'t exists')
            return redirect('reset')
    else:
        return render(request,'resetpass.html')


def viewProfile(request):

    customer=Customer.objects.get(user_id=request.user.id)
    return render(request,'viewProfile.html',{'customer':customer})