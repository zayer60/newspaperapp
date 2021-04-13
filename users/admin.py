from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .form import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email', 'age', 'is_staff',]


admin.site.register(CustomUser, CustomAdmin)
