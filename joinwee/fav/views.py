# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse, Http404
from django.shortcuts import get_object_or_404

from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from fav.models import Fav, Join


@login_required
def fav(request, app, pk):
    ct = ContentType.objects.get(app_label=app, model=app)
    obj = ct.get_object_for_this_type(pk=pk)
    if obj:
        fav, created = Fav.objects.get_or_create(
                user = request.user,
                content_type=ct,
                object_pk=obj.pk)
        if not created:
            fav.save()
    else:
        raise Http404
    return HttpResponseRedirect(obj.get_absolute_url())

@login_required
def unfav(request, app, pk):
    ct = ContentType.objects.get(app_label=app, model=app)
    obj = ct.get_object_for_this_type(pk=pk)
    if obj:
        try:
            fav = Fav.objects.get(user=request.user,
                    content_type=ct,
                    object_pk=obj.pk)
            fav.delete()
        except Fav.DoesNotExist:
            pass
    else:
        raise Http404

    return HttpResponseRedirect(obj.get_absolute_url())

@login_required
def join(request, app, pk):
    ct = ContentType.objects.get(app_label=app, model=app)
    obj = ct.get_object_for_this_type(pk=pk) 
    if obj:
        join, created = Join.objects.get_or_create(
                user = request.user,
                content_type=ct,
                object_pk=obj.pk)
        if not created:
            join.save()
    else:
        raise Http404
    return HttpResponseRedirect(obj.get_absolute_url())


@login_required
def unjoin(request, app, pk):
    ct = ContentType.objects.get(app_label=app, model=app)
    obj = ct.get_object_for_this_type(pk=pk)
    if obj:
        try:
            join = Join.objects.get(user=request.user,
                    content_type=ct,
                    object_pk=obj.pk)
            join.delete()
        except Join.DoesNotExist:
            pass
    else:
        raise Http404

    return HttpResponseRedirect(obj.get_absolute_url())
