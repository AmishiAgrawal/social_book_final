from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
# Create your views here.
def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pwd=request.POST['pwd']
        user=User.objects.create_user(username=uname,password=pwd,email=email,first_name=fname,last_name=lname)
        user.save()
        messages.success(request,'sucessfully registered')
        return render(request,'login.html')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'uhome.html')
        else:
            messages.info(request,'Invalid userid and password')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,'sucessfully logout')
    return render(request,'login.html')