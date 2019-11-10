from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import GroceryUser

class GroceryUserCreationForm(UserCreationForm):
    class Meta:
        model = GroceryUser
        fields = ('username', 'email')

class GroceryUserChangeForm(UserChangeForm):
    class Meta:
        model = GroceryUser
        fields = ('username', 'email')