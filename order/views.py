from django.shortcuts import redirect, render

from order.models import Order, OrderDetail
from store.models import Product, Stock
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required(login_url='login')
def makeOrder(request):
    order = Order.objects.all()
    product = Product.objects.all()
    context = {'orders': order, 'products': product}
    return render(request, 'salesperson/makeorder.html', context)

    # ---------------------------------------


@login_required(login_url='login')
def inOrder(request):
    product = Product.objects.all()
    odetail = OrderDetail.objects.latest('id')
    if request.method == 'POST' and 'done' in request.POST:
        lplate = request.POST.get('plnum')
        quantity = request.POST.get('quantity')
        paidprice = request.POST.get('paidprice')
        tnum = request.POST.get('tnum')
        prid = request.POST.get('pid')
        price = request.POST.get('price')
        pro = Product.objects.get(id=prid)
        #models.OrderDetail.objects.get_or_create(licencePlate = lplate, tinNumber = tnum)
        detail = OrderDetail.objects.latest('id')
        print(detail)
        if detail.added:
            models.Order.objects.get_or_create(
                quantity=quantity, amountsPaid=paidprice, price=price, inOrder='True', product_id=pro.id, detail_id=detail.id)
            OrderDetail.objects.filter(id=detail.id).update(added='False')
            return redirect('orderhistory')
        else:
            models.OrderDetail.objects.get_or_create(
                licencePlate=lplate, tinNumber=tnum)
            detaill = OrderDetail.objects.latest('id')
            models.Order.objects.get_or_create(
                quantity=quantity, amountsPaid=paidprice, price=price, inOrder='True', product_id=pro.id, detail_id=detaill.id)
            return redirect('orderhistory')

    elif request.method == 'POST' and 'more' in request.POST:
        lplate = request.POST.get('plnum')
        quantity = request.POST.get('quantity')
        paidprice = request.POST.get('paidprice')
        tnum = request.POST.get('tnum')
        prid = request.POST.get('pid')
        price = request.POST.get('price')
        pro = Product.objects.get(id=prid)
        detail = OrderDetail.objects.latest('id')
        if detail.added:
            models.Order.objects.get_or_create(
                quantity=quantity, amountsPaid=paidprice, price=price, inOrder='True', product_id=pro.id, detail_id=detail.id)
            return redirect('inorder')
        else:
            models.OrderDetail.objects.get_or_create(
                licencePlate=lplate, tinNumber=tnum, added='True')
            detaill = OrderDetail.objects.latest('id')
            models.Order.objects.get_or_create(
                quantity=quantity, amountsPaid=paidprice, price=price, inOrder='True', product_id=pro.id, detail_id=detaill.id)
            return redirect('inorder')
    context = {'products': product, 'odetail': odetail}
    return render(request, 'salesperson/inorder.html', context)


@login_required(login_url='login')
def outOrder(request):
    product = Product.objects.all()
    odetail = OrderDetail.objects.latest('id')
    if request.method == 'POST' and 'done' in request.POST:
        lplate = request.POST.get('plnum')
        quantity = request.POST.get('quantity')
        paidprice = request.POST.get('paidprice')
        tnum = request.POST.get('tnum')
        prid = request.POST.get('pid')
        price = request.POST.get('price')
        pro = Product.objects.get(id=prid)
        s = Stock.objects.get(product_id=pro.id)
        oq = int(quantity)
        sq = int(s.quantity)
        print(type(quantity))
        print(quantity)
        print(type(sq))
        print(sq)
        if sq < oq:
            return redirect('outorder')

        #models.OrderDetail.objects.get_or_create(licencePlate = lplate, tinNumber = tnum)
        detail = OrderDetail.objects.latest('id')
        print(detail)
        if detail.added:
            models.Order.objects.get_or_create(
                quantity=quantity, amountsPaid=paidprice, price=price, outOrder='True', product_id=pro.id, detail_id=detail.id)
            OrderDetail.objects.filter(id=detail.id).update(added='False')
            return redirect('orderhistory')
        else:
            models.OrderDetail.objects.get_or_create(
                licencePlate=lplate, tinNumber=tnum)
            detaill = OrderDetail.objects.latest('id')
            models.Order.objects.get_or_create(
                quantity=quantity, amountsPaid=paidprice, price=price, outOrder='True', product_id=pro.id, detail_id=detaill.id)
            return redirect('orderhistory')

    elif request.method == 'POST' and 'more' in request.POST:
        lplate = request.POST.get('plnum')
        quantity = request.POST.get('quantity')
        paidprice = request.POST.get('paidprice')
        tnum = request.POST.get('tnum')
        prid = request.POST.get('pid')
        price = request.POST.get('price')
        pro = Product.objects.get(id=prid)
        detail = OrderDetail.objects.latest('id')
        if detail.added:
            models.Order.objects.get_or_create(
                quantity=quantity, amountsPaid=paidprice, price=price, outOrder='True', product_id=pro.id, detail_id=detail.id)
            return redirect('outorder')
        else:
            models.OrderDetail.objects.get_or_create(
                licencePlate=lplate, tinNumber=tnum, added='True')
            detaill = OrderDetail.objects.latest('id')
            models.Order.objects.get_or_create(
                quantity=quantity, amountsPaid=paidprice, price=price, outOrder='True', product_id=pro.id, detail_id=detaill.id)
            return redirect('outorder')
    context = {'products': product, 'odetail': odetail}
    return render(request, 'salesperson/outorder.html', context)


@login_required(login_url='login')
def productList(request):
    product = Product.objects.all()
    if request.method == 'POST':
        pname = request.POST.get('pname')
        ptype = request.POST.get('ptype')
        psize = request.POST.get('psize')
        punit = request.POST.get('punit')
        models.Product.objects.get_or_create(
            product_name=pname, product_type=ptype, product_size=psize, unit=punit)
        pro = Product.objects.latest('id')
        models.Stock.objects.get_or_create(product_id=pro.id)
        return redirect('productlist')
    context = {'product': product}
    return render(request, 'salesperson/productlist.html', context)


@login_required(login_url='login')
def orderHistory(request):
    order = Order.objects.order_by('-orderDate').all()
    context = {'orders': order}
    return render(request, 'salesperson/orderhistory.html', context)


@login_required(login_url='login')
def editOrder(request, oid):
    order = Order.objects.filter(id=oid)
    # print(order.detail.id)
    product = Product.objects.all()

  # edit arg endaresaw !!!!!!!!!!!!!!!!!!!!
    if request.method == 'POST':
        detailid = request.POST.get('did')
        lplate = request.POST.get('plnum')
        tnum = request.POST.get('tnum')
        OrderDetail.objects.filter(id=detailid).update(
            licencePlate=lplate, tinNumber=tnum)
        d = OrderDetail.objects.get(id=detailid)
        quantity = request.POST.get('qty')
        print(quantity)
        paidprice = request.POST.get('paidprice')
        prid = request.POST.get('pid')
        p = request.POST.get('price')
        pro = Product.objects.get(id=prid)
        s = Stock.objects.get(product_id=pro.id)
        sq = int(s.quantity)
        oq = int(quantity)
        o = Order.objects.get(id=oid)
        if o.outOrder:
            if sq < oq:
                return redirect('orderhistory')
            else:
                Order.objects.filter(id=oid).update(
                    quantity=quantity, amountsPaid=paidprice, price=p, product_id=pro.id, detail_id=d.id)
                return redirect('orderhistory')
        else:
            Order.objects.filter(id=oid).update(
                quantity=quantity, amountsPaid=paidprice, price=p, product_id=pro.id, detail_id=d.id)
            return redirect('orderhistory')
    context = {'order': order, 'product': product}
    return render(request, 'salesperson/editorder.html', context)


@login_required(login_url='login')
def cancel(request):
    detail = OrderDetail.objects.latest('id')
    OrderDetail.objects.filter(id=detail.id).update(added='False')
    return redirect('makeorder')
