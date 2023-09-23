from django.contrib import admin
from .models import Owner, Product, Lesson

admin.site.register(Owner)
admin.site.register(Product)
admin.site.register(Lesson)

# from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'name_user', ]


admin.site.register(CustomUser,CustomUserAdmin)

