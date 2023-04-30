from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Category, Product
from .forms import UserForm


def login_page(request):
    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return home(request)
    return render(request, 'login.html')


def login_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            user = authenticate(username=username, password=password)
            if user is None:
                user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                                last_name=lastname)
                user.save()
                return render(request, 'success_register.html')
    else:
        form = UserForm()
    return render(request, 'login.html', {'form': form})


def login_register_view(request):
    return render(request, 'register.html')


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'category': categories, 'products': products})


def caini(request):
    products = Product.objects.filter(category=1)
    return render(request, 'category.html', {'products': products})


def pisici(request):
    products = Product.objects.filter(category=2)
    return render(request, 'category.html', {'products': products})


def rozatoare(request):
    products = Product.objects.filter(category=3)
    return render(request, 'category.html', {'products': products})


def reptile(request):
    products = Product.objects.filter(category=4)
    return render(request, 'category.html', {'products': products})


def pasari(request):
    products = Product.objects.filter(category=5)
    return render(request, 'category.html', {'products': products})


def animaleDeFerma(request):
    products = Product.objects.filter(category=6)
    return render(request, 'category.html', {'products': products})


def product_detail(request, slug):
    products = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'product_detail.html', {'product': products})
