# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20170929_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='thumbnail',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='thumbnails/'),
        ),
    ]
