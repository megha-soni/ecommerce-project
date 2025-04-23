from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import CategoryForm, ProductForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration (optional)
            return redirect('dashboard')  # or wherever you want to redirect
    else:
        form = RegisterForm()
    return render(request, 'product/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'product/dashboard.html')

@login_required
def category_list(request):
    categories = Category.objects.filter(vendor=request.user)
    return render(request, 'product/category_list.html', {'categories': categories})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.vendor = request.user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'product/add_category.html', {'form': form})

@login_required
def product_list(request):
    products = Product.objects.filter(vendor=request.user)
    return render(request, 'product/product_list.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user
            product.save()
            form.save_m2m()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})
