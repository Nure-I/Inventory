# Generated by Django 3.2.9 on 2021-11-10 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_stock_qunit'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='cquantity',
            field=models.CharField(default='0', max_length=50, null=True),
        ),
    ]
