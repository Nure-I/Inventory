# Generated by Django 3.2.9 on 2021-11-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_stock_cquantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
