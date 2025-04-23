from django import forms
from .models import Product, Category
from django.contrib.auth.models import User
from taggit.forms import TagField
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProductForm(forms.ModelForm):
    tags = TagField(required=False)
    class Meta:
        model = Product
        fields = ['name', 'category', 'image', 'price', 'tags']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
