# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models
# from users.models import UserProfile
from guests.models import GuestProfile
# from users.models import UserProfile
from product.models import Product

# Create your models here.

class Order(models.Model):
    from .orderLang import lang2
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,verbose_name = "Ürün/Product")
    guestProfile = models.ForeignKey(GuestProfile,verbose_name = "Misafir Profil/Guest Profile",blank = True,null = True)
    # userProfile = models.ForeignKey(UserProfile,verbose_name = "Kullanıcı Profil/User Profile",blank = True,null = True)
    
    user = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı/User",default = False,blank = True,null = True)
    title = models.CharField(max_length = 100,verbose_name = lang2['title'])
    productImage = models.ImageField(blank = True,null = True,verbose_name = "Resim Ekle/Add Picture")
    productAmount = models.IntegerField(default = 1,verbose_name="Ürün Miktarı/Product Amount")
    totalPrice = models.FloatField(blank = False,null = False,verbose_name = "Fiyat/Price")
    orderedDate = models.DateTimeField(default = '',verbose_name = lang2['orderedDate'])
    orderStatus = models.CharField(max_length = 100,default = "Sipariş Alındı.",verbose_name = lang2['orderStatus'])
    isGuest = models.BooleanField(verbose_name = "Misafir/Guest",default=False)
    isFinished = models.BooleanField(verbose_name = "Tamamlandı Mı?",default=False)
    
    def __str__(self):
        return "ID : {} - Title: {} - Product Amount: {} - Total Price: {} - Ordered Date: {} - Order Status: {}".format(self.id,self.title,self.productAmount,self.totalPrice,self.orderedDate,self.orderStatus)