# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100,verbose_name = "İsim/Name")
    ingredientImage = models.ImageField(blank = True,null = True,verbose_name = "Resim Ekle/Add Picture")

    def __str__(self):
        return "ID : {} - Name: {} - Image: {}".format(self.id,self.name,self.ingredientImage)