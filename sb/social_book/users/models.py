from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from django.utils import timezone

class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)

    fullname = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100 , default='',null=True,blank=True)
    state = models.CharField(max_length=500, default='',null=True,blank=True)
    ccnumber = models.CharField(null=True,blank=True,max_length=30)
    cvc = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=50,null=True,blank=True)
    cctype = models.CharField(max_length=50,null=True,blank=True)
    expdate = models.CharField(null=True,blank=True,max_length=10)
   
    address = models.CharField(max_length=100,default="India")
    public_visibility = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = "username" # make the user log in with the email
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    

class Uploaded_Files(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    desc = models.TextField(max_length=1500)
    visibility = models.BooleanField(default=True)
    price = models.IntegerField(default='1000')
    publish_year = models.CharField(default=' ',max_length=10)
    cover = models.ImageField(upload_to='media/covers/')
    pdf = models.FileField(upload_to='media/pdfs/')

    def __str__(self):
        return self.title
