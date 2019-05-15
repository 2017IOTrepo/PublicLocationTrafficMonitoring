# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from loginfunction import models


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.user.objects.get(userid=username)
            except:
                return render(request, 'login.html')
            if user.password == password:
                return redirect('/index/')  # 重定向
            else:
                message = "用户名或密码错误"
                return render(request, 'login.html', {"message": message})
        return redirect('/index/')
    return render(request, 'login.html')


def index(request):
    return render(request,'index.html')
# Create your views here.
