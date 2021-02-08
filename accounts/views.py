from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import OrdersFilter
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    form = UserRegistrationForm()
    template = 'accounts/register.html'
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request, template, context)


def login(request):
    template = 'accounts/login.html'
    context = {}
    return render(request, template, context)


def index(request):
    orders = Orders.objects.all().order_by('-id')
    customers = Customer.objects.all()
    total_orders = orders.count()
    pending_orders = orders.filter(status='Pending').count()
    delivered_orders = orders.filter(status='Delivered').count()
    template = 'accounts/dashboard.html'
    context = {
        'orders': orders,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
        'customers': customers,
    }
    return render(request, template, context)


def products(request):
    products = Product.objects.all()
    template = 'accounts/products.html'
    context = {
        'products': products
    }
    return render(request, template, context)


def customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    orders = customer.orders_set.all()
    myFilter = OrdersFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    template = 'accounts/customer.html'
    context = {
        'customer': customer,
        'orders': orders,
        'myFilter': myFilter
    }
    return render(request, template, context)


def create_order(request):
    form = OrderForm()
    template = 'accounts/order_form.html'
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')

    return render(request, template, context)


def update_order(request, pk):
    order = Orders.objects.get(pk=pk)
    form = OrderForm(instance=order)
    template = 'accounts/order_form.html'
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    return render(request, template, context)


def delete_order(request, pk):
    Orders.objects.get(pk=pk).delete()
    return redirect('accounts:index')


def create_customer(request):
    form = CustomerForm()
    template = 'accounts/customer_form.html'
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')

    return render(request, template, context)


def update_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    form = CustomerForm(instance=customer)
    template = 'accounts/customer_form.html'
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    return render(request, template, context)


def delete_customer(request, pk):
    Customer.objects.get(pk=pk).delete()
    return redirect('accounts:index')


def create_product(request):
    form = ProductForm()
    template = 'accounts/product_form.html'
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:products')

    return render(request, template, context)


def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(instance=product)
    template = 'accounts/product_form.html'
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('accounts:products')
    return render(request, template, context)


def delete_product(request, pk):
    Product.objects.get(pk=pk).delete()
    return redirect('accounts:products')
