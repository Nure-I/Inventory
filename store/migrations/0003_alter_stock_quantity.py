# Generated by Django 3.2.9 on 2021-11-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.CharField(default='0', max_length=50, null=True),
        ),
    ]
