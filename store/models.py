from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Catagory(models.Model):
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.title}'

class Product(models.Model):
    
    #catagory = models.ForeignKey(Catagory, on_delete=models.DO_NOTHING, null=True)
    product_name = models.CharField(max_length=100, null=True)
    product_type = models.CharField(max_length=100)
    product_size = models.CharField(max_length=50, null=True)
    unit = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'{self.product_name}, {self.product_type} {self.product_size} {self.unit}'

class Stock(models.Model):
    product = models.ForeignKey(Product , on_delete = CASCADE)
    quantity = models.CharField(max_length=50, null=True, default= '0')
    cquantity = models.CharField(max_length=50, null=True, default= '0')
    qunit = models.CharField(max_length=10, default='kuntal')
    def __str__(self):
        return f'{self.product}'