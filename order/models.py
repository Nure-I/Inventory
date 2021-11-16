from django.db import models
from django.db.models.fields import DateTimeCheckMixin, DateTimeField
#from django.db.models.fields import DateTimeField
from store.models import Product, Stock
#from .models import OrderProduct
from datetime import datetime
# Create your models here.

class OrderDetail(models.Model):
    licencePlate = models.IntegerField()
    tinNumber = models.IntegerField()
    bank = models.CharField(max_length=100)
    price = models.PositiveIntegerField(max_length=20, null=True, default= '0')
    added = models.BooleanField(default=False)
   
   
    def __str__(self):
        return f'{self.id}'

class Order(models.Model):
    detail = models.ForeignKey(OrderDetail, on_delete=models.DO_NOTHING, null=True) 
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    inOrder = models.BooleanField(default=False)
    outOrder = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(max_length = 20, null=True, default= '0')
    cquantity = models.PositiveIntegerField(max_length=50, null=True, default= '0')
    price = models.PositiveIntegerField(max_length=20, null=True, default= '0')
    amountsPaid = models.PositiveIntegerField(max_length=20, null=True, default= '0')
    orderDate = models.DateTimeField(default= datetime.now, blank=True) 
    #orderDate = models.DateTimeField(default= DateTimeField.now, blank=True) 
    status = models.CharField(max_length=100, default='pending')
    action = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product}'


