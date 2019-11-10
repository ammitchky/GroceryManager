from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import GroceryUserCreationForm, GroceryUserChangeForm
from .models import GroceryUser


class GroceryUserAdmin(UserAdmin):
    add_form = GroceryUserCreationForm
    form = GroceryUserChangeForm
    model = GroceryUser
    list_display = [
        "email",
        "username",
    ]


admin.site.register(GroceryUser, GroceryUserAdmin)
