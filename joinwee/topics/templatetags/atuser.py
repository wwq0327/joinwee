# -*- coding: utf-8 -*-

import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def atuser(value):
    pat = re.compile(r'@(?P<username>\S+ )')
    
    html = pat.sub(r'<a href="/accounts/\g<username>/">@\g<username> </a>', value)
    return mark_safe(html)
