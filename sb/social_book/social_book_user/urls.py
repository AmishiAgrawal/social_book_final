from django.urls import path
from .import views

urlpatterns = [
    path('home',views.uhome),
    path('register',views.register),
    path('login',views.login),
]
