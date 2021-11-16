from django.contrib.auth.backends import UserModel
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from order.models import Order
from store.models import Product, Stock
from django.contrib import messages
from notifications.signals import notify
# Create your views here.

# -------------------------------------------------------------


# ---------------------------------------------------------
@login_required(login_url='login')
def gebiOrders(request):
    order = Order.objects.filter(inOrder='True')
    context = {'orders': order}
    return render(request, 'warehouse1/gebiorders.html', context)


@login_required(login_url='login')
def wechiOrders(request):
    order = Order.objects.filter(outOrder='True')
    context = {'orders': order}
    return render(request, 'warehouse1/wechiorders.html', context)


@login_required(login_url='login')
def updateStatus(request, oid):
    order = Order.objects.filter(id=oid)
    if request.method == 'POST':
        status = request.POST.get('status')
        order = Order.objects.filter(id=oid).update(status=status)
        sender = User.objects.get(username=request.user)
        receiver = User.objects.get(username='Bilal')
        notify.send(sender, recipient=receiver, verb='Message',
                    description='New order '+ order.product +'has arrived')

        return redirect('wh1index')

    #     ## redirect siyareg previously wedenebberebet endimmels attrsa!!!!!!!!!!!

    # return redirect('gebiOrders')
    context = {'order': order}
    return render(request, 'warehouse1/acceptorder.html', context)


@login_required(login_url='login')
def confirmOrder(request, oid):
    order = Order.objects.filter(id=oid)
    context = {'order': order}
    return render(request, 'warehouse2/confirmorder.html', context)


@login_required(login_url='login')
def confirmQuantity(request, oid):

    order = Order.objects.get(id=oid)
    product = Stock.objects.get(id=order.product.id)

    if order.inOrder:
        if request.method == 'POST':
            cQuantity = request.POST.get('csize')

            # get the quantity of the product and add the value of cQuantity and save

            total = int(product.quantity) + int(cQuantity)
            product.quantity = total
            product.cquantity = cQuantity
            product.save()
            Order.objects.filter(id=oid).update(status='completed')
            Order.objects.filter(id=oid).update(cquantity=cQuantity)
            sender = User.objects.get(username=request.user)
            receiver = User.objects.get(username='Leyla')
            notify.send(sender, recipient=receiver, verb='Message',
                        description='Your order ' + pro + ' has stocked')
            return redirect('wh2index')
    elif order.outOrder:
        if request.method == 'POST':
            cQuantity = request.POST.get('csize')

            # get the quantity of the product and add the value of cQuantity and save

            total = int(product.quantity) - int(cQuantity)
            product.quantity = total
            product.cquantity = cQuantity
            product.save()
            Order.objects.filter(id=oid).update(status='completed')
            Order.objects.filter(id=oid).update(cquantity=cQuantity)
            sender = User.objects.get(username=request.user)
            receiver = User.objects.get(username='Leyla')
            notify.send(sender, recipient=receiver, verb='Message',
                        description='Your order ' + pro + ' has loaded')
            return redirect('wh2index')


def seen(request):
    #Notification.objects.filter(id =nid).update(deleted=True)
    return redirect('/')
