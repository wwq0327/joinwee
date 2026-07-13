#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-22 21:21:01

from django.conf.urls import *

urlpatterns = patterns('',
        url(r'^$', 'home.views.index'),
        url(r'^succ/$', 'home.views.succ'),
        url(r'^about/$', 'home.views.about'),
)

