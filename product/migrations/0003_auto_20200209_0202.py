# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-08 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_ordereddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='orderedDate',
            field=models.DateTimeField(default='', verbose_name=b'Ordered Date'),
        ),
    ]