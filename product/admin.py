# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product
# Register your models here.

# admin.site.register(Article)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","title","productPrice","isPrivate","productImage"]
    list_display_links = ["title","productPrice"]
    search_fields = ["id","title",'productPrice']
    list_filter = ["id","productPrice"]
    
    class Meta:
        model = Product

