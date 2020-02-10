
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models
from product.models import Product
from order.models import Order
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.



class UserProfile(models.Model):
    from .userLang import lang2
    user = models.OneToOneField(User)
    # username2 = models.CharField(max_length = 30,verbose_name = lang2['username'])
    # email = models.EmailField(max_length = 70,verbose_name = lang2['email'])
    # name = models.CharField(max_length = 30,verbose_name = lang2['firstname'])
    # surname = models.CharField(max_length = 30,verbose_name = lang2['lastname'])
    firstName = models.CharField(blank = False,null = False,max_length = 100,default = "", verbose_name = "Adınız/Name")
    lastName = models.CharField(blank = False,null = False,max_length = 100,default = "", verbose_name = "Soyadınız/Lastname")
    phone = models.CharField(default = 0,max_length = 11,verbose_name = "Telefon Numarasi/Phone Number")
    address = models.TextField(default = "",blank = False,null = False, help_text='Adres')
    
    
    completedOrders = models.ManyToManyField(Order, blank = True,related_name = "Tamamlanan Siparisler/Completed Orders+")
    currentOrders = models.ManyToManyField(Order, blank = True,related_name = "Simdiki Siparisler/Current Orders+")
    profileImage = models.ImageField(upload_to = 'profileimg',blank = True,null = True,verbose_name = "Resim Ekle/Add Picture")
    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if(kwargs['created']):
        userProfile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender = User)

