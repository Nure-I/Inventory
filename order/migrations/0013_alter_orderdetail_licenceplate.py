# Generated by Django 3.2.9 on 2021-11-12 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_alter_orderdetail_licenceplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='licencePlate',
            field=models.IntegerField(),
        ),
    ]
