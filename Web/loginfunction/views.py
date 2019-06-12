# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
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
        counts = data.objects.order_by('-id')
        count = counts[0]
        # print(count.time)
        datas = [
            [abnormal.time, abnormal.location, abnormal.pedestrian_flow, "已上传" if (abnormal.is_overloading) else "未上传"]
            for abnormal in counts]
        viewdata = data.objects.filter(location="餐厅").order_by("-id")[:13]
        viewdata_2 = data.objects.filter(location="宿舍").order_by("-id")[:13]
        viewdata_3 = data.objects.filter(location="图书馆").order_by("-id")[:13]
        context = [[i.time] for i in viewdata]
        context_2 = [[i.pedestrian_flow] for i in viewdata]
        context_canting = [[i.time] for i in viewdata]
        context_canting_2 = [[i.pedestrian_flow] for i in viewdata]
        context_sushe = [[i.time] for i in viewdata_2]
        context_sushe_2 = [[i.pedestrian_flow] for i in viewdata_2]
        context_tushuguan = [[i.time] for i in viewdata_3]
        context_tushuguan_2 = [[i.pedestrian_flow] for i in viewdata_3]
        json_data_time_1 = json.dumps(context_canting)
        json_data_data_1 = json.dumps(context_canting_2)
        json_data_time_2 = json.dumps(context_sushe)
        json_data_data_2 = json.dumps(context_sushe_2)
        json_data_time_3 = json.dumps(context_tushuguan)
        json_data_data_3 = json.dumps(context_tushuguan_2)
        json_data_time = json.dumps(context)
        json_data_data = json.dumps(context_2)
        current_count = context_2[0][0]
        current_time = context[0][0]
        yuzhi = ThresholdValue.objects.get(id=1)
        yuzhi_json_yellow = json.dumps(yuzhi.threshold_value_yellow)
        yuzhi_json_normal = json.dumps(yuzhi.threshold_value_normal)
        # 下面为charts2的时间以及数据
        d = datetime.datetime.now()
        d1 = d - datetime.timedelta(days=1)
        d2 = d - datetime.timedelta(days=2)
        d3 = d - datetime.timedelta(days=3)
        d4 = d - datetime.timedelta(days=4)
        d5 = d - datetime.timedelta(days=5)
        d6 = d - datetime.timedelta(days=6)
        day = str(d.strftime("%m-%d"))
        day1 = str(d1.strftime("%m-%d"))
        day2 = str(d2.strftime("%m-%d"))
        day3 = str(d3.strftime("%m-%d"))
        day4 = str(d4.strftime("%m-%d"))
        day5 = str(d5.strftime("%m-%d"))
        day6 = str(d6.strftime("%m-%d"))
        a = []
        a.append(day6)
        a.append(day5)
        a.append(day4)
        a.append(day3)
        a.append(day2)
        a.append(day1)
        a.append(day)
        json_data_date = json.dumps(a)
    except:
        return render(request, 'index.html',
                      {
                          "json_data_time": json_data_time,
                          "json_data_data": json_data_data,
                          "json_data_data_1": json_data_data_1,
                          "json_data_time_1": json_data_time_1,
                          "json_data_data_2": json_data_data_2,
                          "json_data_time_2": json_data_time_2,
                          "json_data_data_3": json_data_data_3,
                          "json_data_time_3": json_data_time_3,
                          "current_count": current_count,
                          "current_time": current_time,
                          "yuzhi": yuzhi,
                          "yuzhi_json_yellow": yuzhi_json_yellow,
                          "yuzhi_json_normal": yuzhi_json_normal,
                          "json_data_date": json_data_date,
                      })
    if count.pedestrian_flow > 0 and datas != None:
        return render(request, 'index.html', {'count': count,
                                              "datas": datas,
                                              "json_data_time": json_data_time,
                                              "json_data_data": json_data_data,
                                              "json_data_data_1": json_data_data_1,
                                              "json_data_time_1": json_data_time_1,
                                              "json_data_data_2": json_data_data_2,
                                              "json_data_time_2": json_data_time_2,
                                              "json_data_data_3": json_data_data_3,
                                              "json_data_time_3": json_data_time_3,
                                              "current_count": current_count,
                                              "current_time": current_time,
                                              "yuzhi": yuzhi,
                                              "yuzhi_json_yellow": yuzhi_json_yellow,
                                              "yuzhi_json_normal": yuzhi_json_normal,
                                              "json_data_date": json_data_date,
                                              })
    else:
        return render(request, 'index.html',
                      {"datas": datas,
                       "json_data_time": json_data_time,
                       "json_data_data": json_data_data,
                       "json_data_data_1": json_data_data_1,
                       "json_data_time_1": json_data_time_1,
                       "json_data_data_2": json_data_data_2,
                       "json_data_time_2": json_data_time_2,
                       "json_data_data_3": json_data_data_3,
                       "json_data_time_3": json_data_time_3,
                       "current_count": current_count,
                       "current_time": current_time,
                       "yuzhi": yuzhi,
                       "yuzhi_json_yellow": yuzhi_json_yellow,
                       "yuzhi_json_normal": yuzhi_json_normal,
                       "json_data_date": json_data_date,
                       })


def charts(request):
    viewdata = data.objects.all().order_by("-time")[:13]
    context = [[i.time] for i in viewdata]
    context_2 = [[i.pedestrian_flow] for i in viewdata]
    json_data_time = json.dumps(context)
    json_data_data = json.dumps(context_2)
    viewdata = data.objects.filter(location="餐厅").order_by("-id")[:13]
    viewdata_2 = data.objects.filter(location="宿舍").order_by("-id")[:13]
    viewdata_3 = data.objects.filter(location="图书馆").order_by("-id")[:13]
    context = [[i.time] for i in viewdata]
    context_2 = [[i.pedestrian_flow] for i in viewdata]
    context_canting = [[i.time] for i in viewdata]
    context_canting_2 = [[i.pedestrian_flow] for i in viewdata]
    context_sushe = [[i.time] for i in viewdata_2]
    context_sushe_2 = [[i.pedestrian_flow] for i in viewdata_2]
    context_tushuguan = [[i.time] for i in viewdata_3]
    context_tushuguan_2 = [[i.pedestrian_flow] for i in viewdata_3]
    json_data_time_1 = json.dumps(context_canting)
    json_data_data_1 = json.dumps(context_canting_2)
    json_data_time_2 = json.dumps(context_sushe)
    json_data_data_2 = json.dumps(context_sushe_2)
    json_data_time_3 = json.dumps(context_tushuguan)
    json_data_data_3 = json.dumps(context_tushuguan_2)
    current_count = context_2[0][0]
    current_time = context[0][0]
    yuzhi = ThresholdValue.objects.get(id=1)
    yuzhi_json_yellow = json.dumps(yuzhi.threshold_value_yellow)
    yuzhi_json_normal = json.dumps(yuzhi.threshold_value_normal)
    # 下面为charts2的时间以及数据
    d = datetime.datetime.now()
    d1 = d - datetime.timedelta(days=1)
    d2 = d - datetime.timedelta(days=2)
    d3 = d - datetime.timedelta(days=3)
    d4 = d - datetime.timedelta(days=4)
    d5 = d - datetime.timedelta(days=5)
    d6 = d - datetime.timedelta(days=6)
    day = str(d.strftime("%m-%d"))
    day1 = str(d1.strftime("%m-%d"))
    day2 = str(d2.strftime("%m-%d"))
    day3 = str(d3.strftime("%m-%d"))
    day4 = str(d4.strftime("%m-%d"))
    day5 = str(d5.strftime("%m-%d"))
    day6 = str(d6.strftime("%m-%d"))
    a = []
    a.append(day6)
    a.append(day5)
    a.append(day4)
    a.append(day3)
    a.append(day2)
    a.append(day1)
    a.append(day)
    json_data_date = json.dumps(a)
    # 下面为每天的人流量平均数据
    people_data_list = []
    shuju_1 = data.objects.filter(time__contains=day6)
    shuju_2 = data.objects.filter(time__contains=day5)
    shuju_3 = data.objects.filter(time__contains=day4)
    shuju_4 = data.objects.filter(time__contains=day3)
    shuju_5 = data.objects.filter(time__contains=day2)
    shuju_6 = data.objects.filter(time__contains=day1)
    shuju_7 = data.objects.filter(time__contains=day)
    count_p = 0
    for i in shuju_1:
        count_p += int(i.pedestrian_flow)
    if (shuju_1.count() == 0):
        people_data_1 = 0
    else:
        people_data_1 = int(count_p) / int(shuju_1.count())
    people_data_list.append(people_data_1)
    count_p = 0
    for i in shuju_2:
        count_p += i.pedestrian_flow
    if (shuju_1.count() == 0):
        people_data_2 = 0
    else:
        people_data_2 = int(count_p) / int(shuju_2.count())
    people_data_list.append(people_data_2)
    count_p = 0
    for i in shuju_3:
        count_p += i.pedestrian_flow
    if (shuju_3.count() == 0):
        people_data_3 = 0
    else:
        people_data_3 = int(count_p) / int(shuju_3.count())
    people_data_list.append(people_data_3)
    count_p = 0
    for i in shuju_4:
        count_p += i.pedestrian_flow
    if (shuju_4.count() == 0):
        people_data_4 = 0
    else:
        people_data_4 = int(count_p) / int(shuju_4.count())
    people_data_list.append(people_data_4)
    count_p = 0
    for i in shuju_5:
        count_p += i.pedestrian_flow
    if (shuju_5.count() == 0):
        people_data_5 = 0
    else:
        people_data_5 = int(count_p) / int(shuju_5.count())
    people_data_list.append(people_data_5)
    count_p = 0
    for i in shuju_6:
        count_p += i.pedestrian_flow
    if (shuju_6.count() == 0):
        people_data_6 = 0
    else:
        people_data_6 = int(count_p) / int(shuju_6.count())
    people_data_list.append(people_data_6)
    count_p = 0
    for i in shuju_7:
        count_p += i.pedestrian_flow
    if (shuju_7.count() == 0):
        people_data_7 = 0
    else:
        people_data_7 = int(count_p) / int(shuju_7.count())
    people_data_list.append(people_data_7)
    red_day = 0
    yellow_day = 0
    green_day = 0
    for i in people_data_list:
        if i > int(yuzhi_json_yellow):
            red_day += 1
        elif i > int(yuzhi_json_normal):
            yellow_day += 1
        else:
            green_day += 1
    people_data = json.dumps(people_data_list)
    return render(request, "charts.html",
                  {"json_data_time": json_data_time,
                   "json_data_data": json_data_data,
                   "json_data_data_1": json_data_data_1,
                   "json_data_time_1": json_data_time_1,
                   "json_data_data_2": json_data_data_2,
                   "json_data_time_2": json_data_time_2,
                   "json_data_data_3": json_data_data_3,
                   "json_data_time_3": json_data_time_3,
                   "current_time": current_time,
                   "current_count": current_count,
                   "yuzhi": yuzhi,
                   "yuzhi_json_yellow": yuzhi_json_yellow,
                   "yuzhi_json_normal": yuzhi_json_normal,
                   "json_data_date": json_data_date,
                   "people_data": people_data,
                   "green_day": green_day,
                   "yellow_day": yellow_day,
                   "red_day": red_day,
                   })


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
            message = user_form.errors
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


def Flow_trend(request):
    d = datetime.datetime.now()
    d1 = d - datetime.timedelta(days=1)
    d2 = d - datetime.timedelta(days=2)
    d3 = d - datetime.timedelta(days=3)
    d4 = d - datetime.timedelta(days=4)
    d5 = d - datetime.timedelta(days=5)
    d6 = d - datetime.timedelta(days=6)
    day1 = str(d1.strftime("%m-%d"))
    day2 = str(d2.strftime("%m-%d"))
    day3 = str(d3.strftime("%m-%d"))
    day4 = str(d4.strftime("%m-%d"))
    day5 = str(d5.strftime("%m-%d"))
    day6 = str(d6.strftime("%m-%d"))
    a = []
    a.append(day6)
    a.append(day5)
    a.append(day4)
    a.append(day3)
    a.append(day2)
    a.append(day1)
