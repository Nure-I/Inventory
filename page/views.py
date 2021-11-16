from django.shortcuts import render
from order.models import Order, Product
from django.contrib.auth.decorators import login_required
from store.models import Stock
from django.contrib import messages
from account.decorators import unauthenticated_user, allowed_user
# Create your views here.


@unauthenticated_user
def login(request):
    return render(request, 'page/login.html')

# @login_required(login_url='login')


@allowed_user(allowed_roles=['sales'])
def spindex(request):
    stock = Stock.objects.all()
    pendingOrder = Order.objects.filter(status='pending').count()
    acceptedOrder = Order.objects.filter(status='accepted').count()
    completedOrder = Order.objects.filter(status='completed').count()

    context = {'stocks': stock, 'pendingOrder': pendingOrder,
               'acceptedOrder': acceptedOrder, 'completedOrder': completedOrder}
    return render(request, 'salesperson/spindex.html', context)


@login_required(login_url='login')
def shindex(request):
    stock = Stock.objects.all()
    pendingOrder = Order.objects.filter(status='pending').count()
    acceptedOrder = Order.objects.filter(status='accepted').count()
    completedOrder = Order.objects.filter(status='completed').count()
    context = {'stocks': stock, 'pendingoOrder': pendingOrder,
               'acceptedOrder': acceptedOrder, 'completedOrder': completedOrder}
    return render(request, 'shareholder/shindex.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['reception'])
def wh1index(request):
    order = Order.objects.all()
    stock = Stock.objects.all()
    pendingOrder = Order.objects.filter(status='pending').count()
    acceptedOrder = Order.objects.filter(status='accepted').count()
    completedOrder = Order.objects.filter(status='completed').count()
    context = {'orders': order, 'stock': stock, 'pendingOrder': pendingOrder,
               'acceptedOrder': acceptedOrder, 'completedOrder': completedOrder}
    return render(request, 'warehouse1/wh1index.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['stock'])
def wh2index(request):
    order = Order.objects.all()
    context = {'orders': order}
    return render(request, 'warehouse2/wh2index.html', context)


@login_required(login_url='login')
def stock(request):
    stock = Stock.objects.all()
    context = {'stocks': stock}
    return render(request, 'page/stock.html', context)
