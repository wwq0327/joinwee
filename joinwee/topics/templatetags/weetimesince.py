# -*- coding: utf-8 -*-
from django import template
from django.utils.timesince import timesince
from django.utils import formats
from django.utils.dateformat import format, time_format
from django.utils import timezone

register = template.Library()

@register.filter(expects_localtime=True, is_safe=False)
def weetimesince(value, arg=None):
    if value is None:
        return ''
    
    now = timezone.now()
    diff = now - value
    if diff.days >= 3:
        try:
            return formats.date_format(value, arg)
        except AttributeError:
            try:
                return format(value, arg)
            except AttributeError:
                return ''
    else:
        try:
            return timesince(value)+u'前'
        except (ValueError, TypeError):
            return ''
