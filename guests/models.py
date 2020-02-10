
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models
# Create your models here.

class GuestProfile(models.Model):
    # user = models.OneToOneField(User)
    # username2 = models.CharField(max_length = 30,verbose_name = lang2['username'])
    # email = models.EmailField(max_length = 70,verbose_name = lang2['email'])
    # name = models.CharField(max_length = 30,verbose_name = lang2['firstname'])
    # surname = models.CharField(max_length = 30,verbose_name = lang2['lastname'])
    firstName = models.CharField(blank = False,null = False,max_length = 100,default = "", verbose_name = "Adınız/Name")
    lastName = models.CharField(blank = False,null = False,max_length = 100,default = "", verbose_name = "Soyadınız/Lastname")
    phone = models.CharField(default = 0,max_length = 11,verbose_name = "Telefon Numarasi/Phone Number")
    address = models.TextField(default = "",blank = False,null = False, help_text='Adres')

    
    def __str__(self):
        return self.firstName + " - " +  self.lastName + " - " + self.phone + "  - " + self.address
