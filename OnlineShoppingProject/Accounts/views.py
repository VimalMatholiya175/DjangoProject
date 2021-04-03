from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.views import View

from .models import Customer
# Create your views here.


class Login(View):
    returnUrl=None
    
    def post(self,request):
        
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])

        if user is not None:
            auth.login(request,user)
            
            if Login.returnUrl:
                return HttpResponseRedirect(Login.returnUrl)
            else:
                Login.returnUrl=None
                return redirect('/')
        else:
            messages.info(request,'Incorrect Username/Password')
            return redirect('login')
    
    def get(self,request):

        Login.returnUrl=request.GET.get('returnUrl')
        return render(request,'login.html')



class SignUp(View):
    
    def post(self,request):

        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['confirmpassword']
        mobileno=request.POST['mobileno']

        if password==cpassword:

            if User.objects.filter(username=username).exists():    
                messages.info(request,'Username is already taken')
                return redirect('signup')
            
            elif User.objects.filter(email=email).exists():    
                messages.info(request,'Email is already taken')
                return redirect('signup')

            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                user.save()
                customer=Customer(user=user,mobileNo=mobileno)
                customer.save()
                return redirect('login')
        
        else:
            messages.info(request,'Password doesn\'t match')
            return redirect('signup')
    
    def get(self,request):

        return render(request,'signup.html')



def logout(request):
    
    auth.logout(request)
    return redirect('/')



class ViewProfile(View):

    def post(self,request):

        request.user.first_name=request.POST['firstname']
        request.user.last_name=request.POST['lastname']
        request.user.username=request.POST['username']
        request.user.email=request.POST['email']
        request.user.save()
        customer=Customer.objects.get(user_id=request.user.id)
        customer.mobileNo=request.POST['mobileno']
        customer.save()

        return redirect('/accounts/viewProfile')

    def get(self,request):
        
        customer=Customer.objects.get(user_id=request.user.id)
        return render(request,'viewProfile.html',{'customer':customer})