from django.contrib import admin
# from django.contrib.auth.admin import UsserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ("email", "is_staff", "is_active",)
#     list_filter = ("email", "is_staff", "is_active",)
#     fieldsets = (
#     #     (None, {"fields": ("email", "password")}),#add fields here
#     #     ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
#         ('Bank Account Credentials', {"fields": ("email","username", "password")}),
#         ('Personal Information', {"fields": ("fullname","gender", "city",'state',)}),
#         ('Payment Mthod And Info', {"fields": ("cctype","ccnumber", "cvc",'expdate',)}),
#         ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
#     )
#     add_fieldsets = (
#         (None, {"fields": ("email","username", "password1", "password2", "is_staff",
#                 "is_active", "groups", "user_permissions")}),
#         ('Personal Information', {"fields": ("fullname","gender", "city",'state',)}),
#         ('Payment Mthod And Info', {"fields": ("cctype","ccnumber", "cvc",'expdate',)}),
#         # (None, {
#         #     "classes": ("wide",),
#         #     "fields": (
#         #         "email", "password1", "password2", "is_staff",
#         #         "is_active", "groups", "user_permissions"
#         #     )}
#         # ),
#     )
#     search_fields = ("email",)
#     ordering = ("email",)


# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser)