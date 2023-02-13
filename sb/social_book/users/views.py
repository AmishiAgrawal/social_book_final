from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .models import CustomUser, Uploaded_Files
import datetime
from django.contrib.auth import authenticate
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.sql import text

def home(request):
    return render(request,'index2.html')
# Create your views here.
def register(request):
    # print(request.POST)
    if request.method=='POST':        
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
    mybooks = Uploaded_Files.objects.all()
    print(mybooks)
    return render(request,'uploadbooks.html',{'mybooks':mybooks})

def add_books(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        cover = request.POST.get('cover')
        desc = request.POST.get('desc')
        # visibility = request.POST.get('visibility')
        visibility = True
        pdf = request.POST.get('pdf')
        price = request.POST.get('price')
        publish_year = request.POST.get('year')
        book = Uploaded_Files(title=title,author=author,category=category,cover=cover,pdf=pdf,publish_year=publish_year,visibility=visibility,desc=desc,price=price)
        book.save()
        messages.success(request,'Your Book has been added successfully!!!!')
        # Create a form in addbook.html see if it saves in db display the books that user uploaded

    return render(request,'addbook.html')

def sqlengine(request):
    name = 'mydb_1'
    user = 'Amishi_Agrawal'
    password = 'amishi777'
    host = 'database-1.c1ttqa9i87aq.ap-south-1.rds.amazonaws.com'
    port = '5432'
    url = (f'postgresql://{user}:{password}@{host}:{port}/{name}')
    engine = create_engine(url)
    con = engine.connect()
    print(con)
    # s1 = 'SELECT * FROM CustomUser'
    rs = con.execute(text('SELECT * FROM users_uploaded_files WHERE users_uploaded_files.price > 50'))
    for row in rs:
        print(row)
  
    return HttpResponse('Done')



def df(request):
    # creating dataframe of size 10 * 3
    data = [['tom',78,18],['raj',67,17],['roy',98,16],['tim',44,18],['riya',72,18],['harsh',68,18],['sia',48,17],['avni',97,18],['vivek',56,16],['ruma',53,18],]
    df = pd.DataFrame(data, columns=['Name','Marks','Age'])
    print(df)

    # Filtering dataframe based on values greater than some value
    print(df[df.Marks > 70])

    # Filtering dataframe with 2 columns
    print(df[(df.Marks > 70) & (df.Age > 17)])
     
    # replace values within dataframe and print
    print(df.replace(to_replace="tom",
           value="timothy"))
    
    # appending two dataframes with same number of columns
    data = [['lily',68,17],['harry',76,18],['ron',56,16],['ginny',56,18],]
    df2 = pd.DataFrame(data, columns=['Name','Marks','Age'])
    print(df.append(df2, ignore_index=True))
    # print(df)
    return HttpResponse(df)