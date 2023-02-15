from django.contrib import admin
from .models import CustomUser,Uploaded_Files
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Uploaded_Files)