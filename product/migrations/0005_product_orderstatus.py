# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-08 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200209_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='orderStatus',
            field=models.CharField(default='Sipari\u015f Al\u0131nd\u0131.', max_length=100, verbose_name=b'Order Status'),
        ),
    ]