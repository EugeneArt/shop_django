# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_productimage_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_active',
        ),
    ]
