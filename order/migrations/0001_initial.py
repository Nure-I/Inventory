# Generated by Django 3.2.9 on 2021-11-06 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('amounts_paid', models.PositiveIntegerField()),
                ('licencePlate', models.IntegerField()),
                ('tinNumber', models.IntegerField()),
                ('bank', models.CharField(max_length=100)),
                ('status', models.CharField(default='pending', max_length=100)),
                ('action', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.product')),
            ],
        ),
    ]
