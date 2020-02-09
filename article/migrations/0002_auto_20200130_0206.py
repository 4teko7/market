# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-29 23:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='Icerik'),
        ),
        migrations.AlterField(
            model_name='article',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Cretated Name'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Baslik'),
        ),
    ]
