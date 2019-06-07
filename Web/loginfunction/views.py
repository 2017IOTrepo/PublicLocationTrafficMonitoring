# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from loginfunction.models import data, ThresholdValue, user
from .forms import RegistrationForm, LoginForm, Info_from
from django.contrib.auth import authenticate, login


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
    global json_data, json_data_time, json_data_data, current_count
    try:
        counts = data.objects.order_by('-id')[:1]
        count = counts[0]
        print(count.time)
        persons = user().selectall()
        datas = [[person.name, person.local, person.phone, person.wechat] for person in persons]
        viewdata = data.objects.all().order_by("-time")[:14]
        context = [[i.time] for i in viewdata]
        context_2 = [[i.pedestrian_flow] for i in viewdata]
        json_data_time = json.dumps(context)
        json_data_data = json.dumps(context_2)
        current_count = context_2[0][0]
        current_time = context[0][0]
        yuzhi = ThresholdValue.objects.get(id=1)
        yuzhi_json_yellow = json.dumps(yuzhi.threshold_value_yellow)
        yuzhi_json_normal = json.dumps(yuzhi.threshold_value_normal)
    except:
        return render(request, 'index.html', {"json_data_time": json_data_time, "json_data_data": json_data_data,
                                              "current_count": current_count, "current_time": current_time,
                                              "yuzhi": yuzhi, "yuzhi_json_yellow": yuzhi_json_yellow,
                                              "yuzhi_json_normal": yuzhi_json_normal})
    if count.pedestrian_flow > 0 and datas != None:
        return render(request, 'index.html', {'count': count, "datas": datas, "json_data_time": json_data_time,
                                              "json_data_data": json_data_data, "current_count": current_count,
                                              "current_time": current_time, "yuzhi": yuzhi,
                                              "yuzhi_json_yellow": yuzhi_json_yellow,
                                              "yuzhi_json_normal": yuzhi_json_normal})
    else:
        return render(request, 'index.html',
                      {"datas": datas, "json_data_time": json_data_time, "json_data_data": json_data_data,
                       "current_count": current_count, "current_time": current_time, "yuzhi": yuzhi,
                       "yuzhi_json_yellow": yuzhi_json_yellow, "yuzhi_json_normal": yuzhi_json_normal})


def charts(request):
    viewdata = data.objects.all().order_by("-time")[:13]
    context = [[i.time] for i in viewdata]
    context_2 = [[i.pedestrian_flow] for i in viewdata]
    json_data_time = json.dumps(context)
    json_data_data = json.dumps(context_2)
    current_count = data.objects.all().order_by("-time")[:1]
    current_time = context[0][0]
    return render(request, "charts.html",
                  {"json_data_time": json_data_time, "json_data_data": json_data_data, "current_count": current_count,
                   "current_time": current_time})


def tables(request):
    persons = user.objects.all()
    datas = [[person.name, person.local, person.phone, person.wechat] for person in persons]
    return render(request, 'tables.html', context={'datas': datas})


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        new_info_form = Info_from(request.POST)
        if user_form.is_valid() and new_info_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            message = "注册成功，请您进行登录"
            new_info = new_info_form.save(commit=False)
            new_info.user = new_user
            new_info.save()
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
        datas[0].pedestrian_flow,
        datas[0].location
    ]
    return HttpResponse(json.dumps(results), content_type='application/json')
