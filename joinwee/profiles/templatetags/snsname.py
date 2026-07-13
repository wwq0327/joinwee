# -*- coding: utf-8 -*-
from django import template

from django.contrib.auth.models import User
from profiles.models import ConfirEmail

register = template.Library()

@register.filter
def snsname(value):
    value = value.lower()
    if value == 'weibo':
        value = u'新浪微博'
    elif value == 'douban2':
        value = u'豆瓣'
    else:
        value = value

    return value

@register.filter
def ef(value):

    user = User.objects.get(username=value)
    
    ec = ConfirEmail.objects.filter(user__username=value)
    if user.email and not ec:
        return True

    if ec:
        ec = ec.reverse()[0]
        return ec.active
    else:
        return False
    
