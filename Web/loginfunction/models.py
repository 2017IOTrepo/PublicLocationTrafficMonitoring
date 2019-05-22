# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django.db import models
from django import forms
from django.contrib.auth.models import User


class user(models.Model):
    userid = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userid

    class Meta:
        ordering = ['c_time']
        verbose_name = u'用户'
        verbose_name_plural = u'用户'


class human_traffic_count(models.Model):
    count = models.IntegerField()
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"当前人流总数"

    class Meta:
        ordering = ['c_time']
        verbose_name = '人流量'
        verbose_name_plural = '当前人流量'
# Create your models here.
