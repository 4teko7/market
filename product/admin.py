# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product
# Register your models here.

# admin.site.register(Article)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","title","productPrice","createdDate","isPrivate","productImage"]
    list_display_links = ["title","createdDate","productPrice"]
    search_fields = ["id","title",'productPrice']
    list_filter = ["id","createdDate"]
    
    class Meta:
        model = Product

