#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-31 20:47:59

from django import template
from django.contrib.contenttypes.models import ContentType
from weelesson.models import WEELesson
from weemeet.models import WEEMeet

register = template.Library()

@register.filter(name="user_fav")
def user_fav_lesson(app_name):
    pass

