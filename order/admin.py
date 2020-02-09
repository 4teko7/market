# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Order
# Register your models here.

# admin.site.register(Article)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['isFinished',"id","title","productImage",'orderStatus',"productAmount","totalPrice","orderedDate"]
    list_display_links = ["title","productImage"]
    search_fields = ["id","title",'orderStatus']
    list_filter = ["id","orderedDate","orderStatus"]
    
    class Meta:
        model = Order

