# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Ingredient
# Register your models here.

# admin.site.register(Article)
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id',"name"]
    list_display_links = ["name"]
    search_fields = ["id","name"]
    list_filter = ["id","name"]
    
    class Meta:
        model = Ingredient

