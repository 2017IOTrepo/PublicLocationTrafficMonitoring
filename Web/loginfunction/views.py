# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import models
from loginfunction.models import human_traffic_count, data, security_staff
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
import time
from django.forms.models import model_to_dict


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


def index(request):
    try:
        counts = data.objects.order_by('-id')[:1]
        count = counts[0]
        print(count.time)
        persons = security_staff().selectall()
        datas = [[person.name, person.location, person.p_number, person.weixin] for person in persons]
    except:
        return render(request, 'index.html')
    if count.pedestrian_flow > 0 and datas != None:
        return render(request, 'index.html', {'count': count, "datas": datas})
    else:
        return render(request, 'index.html', {"datas": datas})

def charts(request):
   return render(request,"charts.html")


def tables(request):
    persons = security_staff().selectall()
    datas = [[person.name, person.location, person.p_number, person.weixin] for person in persons]
    return render(request, 'tables.html', context={'datas': datas})


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
    if data().insert_data():
        print("True")
    else:
        print("False")
    datas = data.objects.all()[:1]  # 在  前加一个负号，可以实现倒序
    results = [
        datas[0].time,
        datas[0].pedestrian_flow
    ]
    return HttpResponse(json.dumps(results), content_type='application/json')
