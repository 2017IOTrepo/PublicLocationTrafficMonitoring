# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

admin.site.register(models.user)
admin.site.register(models.human_traffic_count)
# Register your models here.
