# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
        verbose_name = '用户'
        verbose_name_plural = '用户'

#地区表
class data(models.Model):
    location=models.CharField(u'地点',max_length=50,null=False) #地点
    pedestrian_flow=models.IntegerField(u'人流量')               #人流量
    is_overloading=models.BooleanField(u'是否超载')                #是否超载
    abnormal_video=models.BinaryField(u'异常视频')                 #异常视频
    time=models.CharField(u'捕获时间',max_length=50,null=False)     #捕获时间

    def __str__(self):
        return self.location

    class Meta:
        db_table='local_data'
        ordering = ['-id']
        verbose_name = '人流量'
        verbose_name_plural = '人流量'

#保安组织人员信息表
class security_staff(models.Model):
    name=models.CharField(u'姓名',max_length=50,null=True)      #名字
    location=models.CharField(u'位置',max_length=50)            #所在地点
    p_number=models.CharField(u'联系方式',max_length=50)            #电话号
    weixin=models.CharField(u'微信',max_length=50,null=True)    #微信号

    class Meta:
        db_table = 'security_staff'
        ordering = ['id']
        verbose_name = '安保人员'
        verbose_name_plural = '安保人员'

    def __str__(self):
        return self.name

    #创建新的人物
    def  insertone(self,**info):
         if security_staff.objects.get_or_create(name=info['name'],
                                              location=info['location'],
                                              p_number=info['p_number'],
                                              weixin=info['weixin']):
             return True
         return False

    #删除人物信息
    def deleteone(self,name):
        if security_staff.objects.filter(name__contains=name).delete():
            return True
        return False

    #显示人员的信息
    def  selectall(self):
        persons=security_staff.objects.all()
        results=[[],[],[],[]]
        i=0;
        for person in persons:
            results[0][i]=person.name
            results[1][i]=person.location
            results[2][i]=person.p_number
            results[3][i]=person.weixin
        return results

    #更改信息
    def upadteone(self,**info):
        one=security_staff.objects.get(info['name'])
        one.location=info['location']
        one.p_number=info['p_number']
        one.weixin=info['weixin']
        one.save()

# Create your models here.
