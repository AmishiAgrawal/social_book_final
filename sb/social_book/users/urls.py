from django.urls import path
from .import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('authorsandsellers/',views.authorsandsellers,name='aanss'),
    path('books/',views.books,name='books'),
    path('add_books/',views.add_books,name='add_books'),
    
]