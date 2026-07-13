#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-22 21:21:01

from django.conf.urls import *

urlpatterns = patterns('',
        url(r'^$', 'weelesson.views.index', name="lesson_index"),
        url(r'^(?P<pk>\d+)/$', 'weelesson.views.lesson', name="weelesson_detail"),
        url(r'^create/$', 'weelesson.views.create', name="lesson_create"),
        url(r'^(?P<pk>\d+)/publish/info/$', 'weelesson.views.info', name="lesson_info"),
        url(r'^(?P<pk>\d+)/publish/$', 'weelesson.views.publish', name="lesson_publish"),
        url(r'^(?P<pk>\d+)/unpublish/$', 'weelesson.views.unpublish', name="lesson_unpublish"),
        url(r'^(?P<pk>\d+)/edit/$', 'weelesson.views.edit', name="lesson_edit"),
        url(r'^(?P<pk>\d+)/del/$', 'weelesson.views.delete', name="lesson_delete"),
        url(r'^', include('fav.urls'), {'app': 'weelesson'}),
        url(r'^(?P<pk>\d+)/draft/$', 'weelesson.views.draft', name="lesson_draft"),
        url(r'^(?P<pk>\d+)/discuss/$', 'topics.views.all', name="t_all"), ##  by topics app
)

