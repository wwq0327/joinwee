# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.utils.http import urlquote, urlunquote
from django.utils.encoding import force_str

from weelesson.models import WEELesson

def tag_item(request, tag):
    _tag = urlunquote(urlunquote(tag) )
    lessons = WEELesson.objects.filter(tags__name__in=[_tag])
    
    return render(request, 'tags/tag_item.html',
            {'lessons': lessons, 'tag': _tag})


