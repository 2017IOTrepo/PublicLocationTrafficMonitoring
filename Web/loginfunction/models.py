# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class user(models.Model):
    userid=models.CharField(max_length=128,unique=True)
    password=models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userid

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
# Create your models here.
