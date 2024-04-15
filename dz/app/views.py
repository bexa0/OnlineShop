from datetime import datetime
from functools import reduce

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from app.models import *


# Create your views here.

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'signin.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('product_list')



class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'
class UserListView(ListView):
    model = User
    template_name = 'users_list.html'
    context_object_name = 'users'


def order_products(request, pk):
    order = Order.objects.get(id=pk)
    products = OrderAndProduct.objects.filter(order=order)

    return render(request, 'order_products.html', context={'order': order, 'products': products})

def delivered(request, pk):
    order = Order.objects.get(id=pk)
    order.status = 'Delivered'
    order.save()
    return redirect('order_list')
def page_delivered(request):
    order = Order.objects.filter(status='Delivered')
    return render(request, 'delivered.html', context={'orders': order})
def user_orders(request, pk):
    context = {'order': Order.objects.get(user=User.objects.get(id=pk)),
               "products": OrderAndProduct.objects.filter(order=Order.objects.get(user=User.objects.get(id=pk)))}
    return render(request, 'user_orders.html', context)

def Order_add(request, pk):
    product_user = Product.objects.get(id=pk)
    user_order = [i.user for i in Order.objects.all()]


    if request.user in user_order:
        order = Order.objects.get(user=request.user)
        order.product.add(product_user)

        orderandproduct = OrderAndProduct.objects.get(order=order, product=product_user)

        orderandproduct.count += 1
        orderandproduct.save()
    else:
        order1 = Order.objects.create(status='New', user=request.user)
        order1.product.add(product_user)

        orderandproduct = OrderAndProduct.objects.get(order=order1, product=product_user)

        orderandproduct.count += 1
        orderandproduct.save()

    gorder = Order.objects.get(user=request.user)
    orderandproduct1 = OrderAndProduct.objects.filter(order=gorder)

    i = [(i.product.price - (i.product.price / 100*i.product.discount)) * i.count for i in orderandproduct1]

    gorder.sum = sum(i)
    gorder.save()
    return redirect('product_list')




def user_logout(request):
    logout(request)
    return redirect('product_list')