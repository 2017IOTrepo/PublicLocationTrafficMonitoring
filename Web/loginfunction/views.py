# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import data,security_staff
import json

# from django.http import HttpResponse

def userlogin(request):
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "login.html")
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user:
                login(request, user)
                return redirect('/index')  # 重定向
            else:
                message = "登录失败，用户名或密码错误，请检查您的用户名密码"
                return render(request, "login.html", {"message": message})
    return redirect('/login')

    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     if username and password:  # 确保用户名和密码都不为空
    #         username = username.strip()
    #         # 用户名字符合法性验证
    #         # 密码长度验证
    #         # 更多的其它验证.....
    #         try:
    #             user = models.user.objects.get(userid=username)
    #         except:
    #             return render(request, 'login.html')
    #         if user.password == password:
    #             return redirect('/index/')  # 重定向
    #         else:
    #             message = "用户名或密码错误"
    #             return render(request, 'login.html', {"message": message})
    #     return redirect('/index/')
    # return render(request, 'login.html')


def index(request):
    persons = security_staff().selectall()
    datas = [[person.name, person.location, person.p_number, person.weixin] for person in persons]
    return render(request, 'index.html', context={'datas': datas})

def charts(request):
   return render(request,"charts.html")


def tables(request):
    persons=security_staff().selectall()
    datas=[[person.name,person.location,person.p_number,person.weixin] for person in persons]
    return render(request, 'tables.html',context={'datas':datas})


# Create your views here.

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            message = "注册成功，请您进行登录"
            return render(request, "register.html", {"message": message})
        else:
            message = "您的输入有误，请重新输入，请检查两次密码是否一致"
            return render(request, "register.html", {"message": message})
    else:
        user_form = RegistrationForm()
        return render(request, "register.html", {"form": user_form})


def clean(request):
    request.session.flush()
    return redirect("http://127.0.0.1:8000/login/")

def part_flush(request):
    datas=data.objects.all()[:13]  # 在  前加一个负号，可以实现倒序
    results=[
        [data.time for data in datas],
        [data.pedestrian_flow for data in datas]
           ]
    return HttpResponse(json.dumps(results), content_type='application/json')
