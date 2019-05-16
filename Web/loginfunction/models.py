# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
<<<<<<< HEAD
from django import forms
from django.contrib.auth.models import User


class user(models.Model):
    userid = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
=======


class user(models.Model):
    userid=models.CharField(max_length=128,unique=True)
    password=models.CharField(max_length=256)
>>>>>>> 54dd4c9c2efebe5e373504f127e4249b0c01bbfe
    email = models.EmailField(unique=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userid

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
<<<<<<< HEAD


=======
>>>>>>> 54dd4c9c2efebe5e373504f127e4249b0c01bbfe
# Create your models here.
