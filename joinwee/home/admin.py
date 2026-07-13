#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-23 21:21:41

from django.contrib import admin
from home.models import First

class FirstAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)

admin.site.register(First, FirstAdmin)
