from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .models import CustomUser, Uploaded_Files
import datetime
from django.contrib.auth import authenticate



# User = settings.AUTH_USER_MODEL
# import social_book.users.models
# AUTH_USER_MODEL = 'users.CustomUser'

def home(request):
    return render(request,'index2.html')
# Create your views here.
def register(request):
    # print(request.POST)
    if request.method=='POST':
        print("Simran")
        
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        fullname=request.POST.get('fullname')
        gender=request.POST.get('gender')
        # print(gender)
        city=request.POST.get('city')
        state=request.POST['state']
        cctype=request.POST.get('cctype')
        # print(cctype)
        ccnumber=request.POST['ccnumber']
        cvc=request.POST['cvc']
        cdate = datetime.datetime(int(request.POST.get('year')), int(request.POST.get('month')), 10)
        expdate = str(cdate.month) + ' - ' + str(cdate.year)
        print(expdate)
        address = city + ', ' + state
        if password != cpassword:
            return HttpResponse('passwords do not match')
        condition = request.POST.get('condition')
        print(condition)
        public_visibility = request.POST.get('public_visibility')
        print(public_visibility)
        # address = models.CharField(max_length=100,default="India")

        if condition == 'agreed':
            db = get_user_model()
            user=db.objects.create_user(email=email,username=username,password=password,fullname=fullname,gender=gender,city=city,state=state,cctype=cctype,ccnumber=ccnumber,cvc=cvc,expdate=expdate,address=address)
            # user=db.objects.create(email=email,username=username,password=password)
            print(user)
            user.set_password(password)
            user.save()
            messages.success(request,'sucessfully registered')
            return render(request,'login.html')
        else:
            messages.warning(request,'Please check the box to show you agree with the terms and conditions.')
            return render(request,'register.html')
    else:
        return render(request,'register.html')
    # return HttpResponse('register')

        # User = get_user_model()
    #     if pwd==cpwd:
    #         if User.objects.filter(username=username).exists():
    #             messages.info(request, 'Email is exist ')
    #             return render(request,'register.html')
    #         else:
    #             user = User.objects.create(username=username,pwd=pwd, email=email)
    #             user.set_password(pwd)
    #             user.save()
    #             messages.success(request,'sucessfully registered')
    #             print("success")
    #             return render(request,'login.html')
    #     else:
    #         messages.info(request, 'Both passwords are not matching')
    #         return render(request,'register.html')
    # else:
    #     print("no post method")
    #     return render(request, 'register.html') 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method=='POST':
        
        uname=request.POST['uname']
        print(uname,'username')
        pwd=request.POST['pwd']
        print(pwd,'password')

        user=auth.authenticate(username=uname,password=pwd)
        print(user,'authenticate')
    
        if user is not None:

            auth.login(request,user)
            return authorsandsellers(request)
            # return render(request,'authandsellers.html')
        else:
            messages.info(request,'Invalid userid and password')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,'sucessfully logout')
    return render(request,'login.html')

def authorsandsellers(request):
    ob = CustomUser.objects.filter(public_visibility=True)
    return render(request,'authandsellers.html',{'ob': ob})

def books(request):
    return render(request,'uploadbooks.html')

def add_books(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        cover = request.POST.get('cover')
        desc = request.POST.get('desc')
        visibility = request.POST.get('visibility')
        pdf = request.POST.get('pdf')
        price = request.POST.get('price')
        publish_year = request.POST.get('publish_year')
        book = Uploaded_Files(title=title,author=author,category=category,cover=cover,pdf=pdf,publish_year=publish_year,visibility=visibility,desc=desc,price=price)
        book.save()
        messages.success(request,'Your Book has been added successfully!!!!')
        # Create a form in addbook.html see if it saves in db display the books that user uploaded

    return render(request,'addbook.html')