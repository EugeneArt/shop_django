# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_productinorder_sub_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=models.CharField(max_length=48),
        ),
    ]
