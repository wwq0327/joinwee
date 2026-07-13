#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-24 13:44:37

from django.contrib import admin
from weelesson.models import WEELesson, FineLesson

admin.site.register(WEELesson)
admin.site.register(FineLesson)
