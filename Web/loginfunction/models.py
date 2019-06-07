# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
import time
import random
from random import choice


class user(models.Model):
    user = models.OneToOneField(User, unique=True,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, null=True)
    local = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    wechat = models.CharField(max_length=50, null=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.id)

    class Meta:
        ordering = ['c_time']
        verbose_name = u'用户'
        verbose_name_plural = u'用户'


    # 创建新的人物
    def insertone(self, **info):
        if user.objects.get_or_create(name=info['name'],
                                                location=info['location'],
                                                p_number=info['p_number'],
                                                weixin=info['weixin']):
            return True
        return False

    # 删除人物信息
    def deleteone(self, name):
        if user.objects.filter(name__contains=name).delete():
            return True
        return False

    # 显示人员的信息
    def selectall(self):
        persons = user.objects.all()
        return persons

    # 更改信息
    def upadteone(self, **info):
        one = user.objects.get(info['name'])
        one.location = info['location']
        one.p_number = info['p_number']
        one.weixin = info['weixin']
        one.save()


class ThresholdValue(models.Model):
    threshold_value_normal = models.IntegerField(u"正常人流阈值", null=False)
    threshold_value_yellow = models.IntegerField(u"人流量黄色阈值", null=False)

    class Meta:
        db_table = 'threshold_value'
        ordering = ['-id']
        verbose_name = '人流量阈值'
        verbose_name_plural = '人流量阈值'


# 地区表
class data(models.Model):
    location = models.CharField(u'地点', max_length=50, null=False)  # 地点
    pedestrian_flow = models.IntegerField(u'人流量')  # 人流量
    is_overloading = models.BooleanField(u'是否超载')  # 是否超载
    abnormal_video = models.CharField(u'异常视频', max_length=50, null=True)  # 异常视频
    time = models.CharField(u'捕获时间', max_length=50, null=False)  # 捕获时间

    def __str__(self):
        return self.location

    class Meta:
        db_table = 'local_data'
        ordering = ['-id']
        verbose_name = '人流量'
        verbose_name_plural = '人流量'

    def insert_data(self, **info):
        info = {'location': choice(["餐厅","宿舍","图书馆"]),
                'pedestrian_flow': random.randint(0, 40000),
                'is_overloading': 1,
                'abnormal_video': None,
                'time': str(time.strftime("%m-%d %H:%M", time.localtime()))}
        if data.objects.get_or_create(location=info['location'],
                                      pedestrian_flow=info['pedestrian_flow'],
                                      is_overloading=info['is_overloading'],
                                      abnormal_video=info['abnormal_video'],
                                      time=info['time']):
            return True
        return False


