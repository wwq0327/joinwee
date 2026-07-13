#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-22 21:21:01

from django.conf.urls import *

urlpatterns = patterns('',

        url(r'^(?P<pk>\d+)/$', 'topics.views.topic', name="t_topic"),
        url(r'^(?P<app>\w+)/(?P<pk>\d+)/create/$', 'topics.views.create', name="t_create"),
        url(r'^(?P<pk>\d+)/edit/$', 'topics.views.edit', name="t_edit"),
        url(r'^(?P<pk>\d+)/del/$', 'topics.views.delete', name="t_delete"),
		url(r'^comment/(?P<pk>\d+)/del/$', 'topics.views.delete_comment', name="cm_del"),
)

