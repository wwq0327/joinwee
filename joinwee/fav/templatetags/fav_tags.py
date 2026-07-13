#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-31 20:47:59

from django import template

register = template.Library()

@register.filter(name="user_fav")
def user_fav_lesson(app_name):
    pass

