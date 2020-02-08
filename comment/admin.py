# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Comment
# Register your models here.

# admin.site.register(Article)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id","author","product","createdDate","comments2"]
    list_display_links = ["id","author","product"]
    search_fields = ["id","author","product"]
    list_filter = ["id","createdDate","author","product"]
    
    class Meta:
        model = Comment

