# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from product.models import Product
from django.contrib.postgres.fields import ArrayField
from .commentLang import commentLanguage
from djangoBlog.language import *
import json
# Create your models here.

class Comment(models.Model):

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name = "Urunler/Product")
    content = models.TextField(max_length = 4000,verbose_name = "Yorum Ekle")
    createdDate = models.DateTimeField(auto_now_add = True,verbose_name = "Oluşturulma Tarihi")
    userImage = models.ImageField(blank = True,null = True,verbose_name = "Resim Ekle/Add Picture")
    
    comments2 = models.TextField(max_length = 4000,blank = True,null = True,verbose_name = "Yorum Ekle")
    def __str__(self):
        return "Id: {} - Author: {} - Created Date: {} - Content : {}".format(self.id,self.author,self.createdDate,self.content)