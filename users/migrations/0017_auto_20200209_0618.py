# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-09 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_userprofile_productamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='completedOrders',
            field=models.ManyToManyField(blank=True, related_name='_userprofile_completedOrders_+', to='order.Order'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='currentOrders',
            field=models.ManyToManyField(blank=True, related_name='_userprofile_currentOrders_+', to='order.Order'),
        ),
    ]
