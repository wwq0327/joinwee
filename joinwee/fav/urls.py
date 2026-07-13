#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-30 20:39:43

from django.conf.urls import *

urlpatterns = patterns('',
        url(r'^(?P<pk>\d+)/fav/$', 'fav.views.fav'),
        url(r'^(?P<pk>\d+)/unfav/$', 'fav.views.unfav'),
        url(r'^(?P<pk>\d+)/join/$', 'fav.views.join'),
        url(r'^(?P<pk>\d+)/unjoin/$', 'fav.views.unjoin'),
)        
