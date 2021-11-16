# Generated by Django 3.2.9 on 2021-11-12 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20211112_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default='0', max_length=20, null=True),
        ),
    ]