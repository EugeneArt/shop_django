# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20170926_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='nmb',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='price_per_item',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='total_price',
        ),
        migrations.AddField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='comment',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
