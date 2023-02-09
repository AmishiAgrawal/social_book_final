from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import login, authenticate
import datetime
from django.contrib import auth

# Create your views here.

def register(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        state = request.POST.get('state')
        cctype = request.POST.get('cctype')
        ccnumber = request.POST.get('ccnumber')
        cvc = request.POST.get('cvc')
        cvc = int(cvc)
        cdate = datetime.datetime(int(request.POST.get('year')), int(request.POST.get('month')), 10)
        expdate = str(cdate.month) + ' - ' + str(cdate.year)
        print(expdate)
        condition = request.POST.get('condition')
        print(condition)
        public_visibility = request.POST.get('public_visibility')
        print(public_visibility)
        # address = models.CharField(max_length=100,default="India")

        if condition == 'agreed':
            db = get_user_model()
            user=db.objects.create_user(fullname=fullname,password=password,username=username, email=email,gender=gender,city=city,state=state,cctype=cctype,ccnumber=ccnumber,cvc=cvc,expdate=expdate,public_visibility=public_visibility)
            print(user)
            user.save()
            messages.success(request,'sucessfully registered')
            return render(request,'login.html')
        else:
            messages.warning(request,'Please check the box to show you agree with the terms and conditions.')
            return render(request,'register.html')
    
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST['uname']
        pwd=request.POST['pwd']
        user=auth.authenticate(email=email,password=pwd)
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