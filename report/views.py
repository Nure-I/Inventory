from typing import ContextManager
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from order.models import Order
from django.contrib import messages
# Create your views here.
@login_required(login_url='login')
def fReport(request):
    return render(request,'report/financialreport.html')

@login_required(login_url='login')
def orderReport(request):
    return render(request,'report/orderreport.html')

@login_required(login_url='login')  
def inOrderDetail(request):
    inorder = Order.objects.filter(inOrder = 'True')
    context = { 'orders': inorder}
    return render(request,'report/inorderdetail.html',context)


@login_required(login_url='login')
def outOrderDetail(request):
    outorder = Order.objects.filter(outOrder = 'True')
    context = { 'orders': outorder}
    return render(request,'report/outorderdetail.html',context)

@login_required(login_url='login')
def detailO(request,oid):
    order = Order.objects.filter(id = oid)
    context = { 'detail': order}
    return render(request,'report/detailO.html',context)
