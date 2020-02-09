
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import GuestProfile

# Register your models here.

# admin.site.register(Article)
@admin.register(GuestProfile)
class GuestAdmin(admin.ModelAdmin):
    list_display = ["firstName","lastName","phone","address"]
    list_display_links = ["firstName","phone"]
    search_fields = ["firstName","phone"]
    list_filter = ["firstName","phone"]
    
    class Meta:
        model = GuestProfile

