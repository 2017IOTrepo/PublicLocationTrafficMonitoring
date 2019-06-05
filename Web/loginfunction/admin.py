# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

admin.site.register(models.user)
admin.site.register(models.data)
admin.site.register(models.ThresholdValue)