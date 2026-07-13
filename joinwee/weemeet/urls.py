#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-22 21:21:01

from django.conf.urls import *

urlpatterns = patterns('',
        #url(r'^$', 'weemeet.views.index', name="meet_index"),
        url(r'^(?P<pk>\d+)/$', 'weemeet.views.detail', name="meet_detail"),
        url(r'^(?P<pk>\d+)/create/$', 'weemeet.views.create', name="meet_create"),
        url(r'^(?P<pk>\d+)/edit/$', 'weemeet.views.edit', name="meet_edit"),
        url(r'^(?P<pk>\d+)/del/$', 'weemeet.views.delete', name="meet_delete"),
        url(r'^', include('fav.urls'), {'app': 'weemeet'}),
)

