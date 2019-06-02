# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

from loginfunction.models import human_traffic_count
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login


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
                return redirect('/index/')  # 重定向
            else:
                message = "登录失败，用户名或密码错误，请检查您的用户名密码"
                return render(request, "login.html", {"message": message})


def index(request):
    data_count = human_traffic_count.objects.all().count()
    count = human_traffic_count.objects.get(id=data_count)
    if count.count > 0:
        return render(request, 'index.html', {'count': count})
    else:
        return render(request, 'index.html')


def charts(request):
    return render(request, 'charts.html')


def tables(request):
    return render(request, 'tables.html')


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
