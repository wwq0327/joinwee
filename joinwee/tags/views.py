# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.utils.http import urlquote, urlunquote
from django.utils.encoding import force_text

from weelesson.models import WEELesson

def tag_item(request, tag):
    _tag = urlunquote(urlunquote(tag) )
    lessons = WEELesson.objects.filter(tags__name__in=[_tag])
    
    return render_to_response('tags/tag_item.html',
            {'lessons': lessons, 'tag': _tag},
            context_instance=RequestContext(request))


