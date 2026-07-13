# -*- coding: utf-8 -*-

import datetime

from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from weelesson.models import WEELesson
from weemeet.models import WEEMeet
from weemeet.forms import WEEMeetForm
from topics.models import Topics
from fav.models import Fav, Join

def index(request):
    '''微聚首页面'''
    by = request.GET.get('order', '')
    now = datetime.datetime.now()
    if by == 'pre':
        meets = WEEMeet.objects.filter(start_time__gt=now) # 开始时间大于现在时间，项目为筹备状态
    elif by == 'pass':
        meets = WEEMeet.objects.filter(end_time__lt=now) # 结束时间小于当前时间，项目为已过状态
    elif by == 'doing':
        meets = WEEMeet.objects.filter(start_time__lt=now) \
                .filter(end_time__gt=now) # 开时时间小于当前时间，结束时间大于当前时间的为进行中的
    else:
        meets = WEEMeet.objects.all()

    return render(request, 'weemeet/index.html',
            {'meets': meets})

@login_required
def create(request, pk):
    '''创建一个微聚'''
    lesson = get_object_or_404(WEELesson, pk=pk)
    if request.method == 'POST':
        form = WEEMeetForm(request.POST, request.FILES)
        if form.is_valid():
            o = form.save(commit=False)
            o.lesson = lesson
            o.creater = request.user
            o.save()

            return HttpResponseRedirect(reverse('meet_detail', args=(o.pk,)))
    else:
        form = WEEMeetForm()

    return render(request, 'weemeet/create.html',
            {'form': form, 'lesson': lesson})

def detail(request, pk):
    meet = get_object_or_404(WEEMeet, pk=pk)
    ct = ContentType.objects.get(app_label='weemeet', model='weemeet')

    try:
        if request.user.is_authenticated:
           fav = request.user.fav_set.get(object_pk=meet.pk, content_type=ct)

           if fav:
               is_fav = True
           else:
               is_fav = False
        else:
            is_fav = False
    except Fav.DoesNotExist:
        is_fav = False

    try:
        if request.user.is_authenticated:
            join = request.user.join_set.get(object_pk=meet.pk, content_type=ct)
            if join:
                is_join = True
            else:
                is_join = False
        else:
            is_join = False
    except Join.DoesNotExist:
        is_join = False

    #topics = Topics.objects.for_model(meet.lesson) #话题都转到相应的微课上去
    favs = Fav.objects.for_model(meet)
    joins = Join.objects.for_model(meet)
    point = "%.2f" % (float(joins.count()/float(meet.number))*100) #取两位小数
    return render(request, 'weemeet/detail.html',
            {
                'meet': meet,
                #'topics': topics,
                'is_fav': is_fav,
                'is_join': is_join,
                'favs': favs,
                'joins': joins,
                'point': point,
                })

@login_required
def edit(request, pk):
    meet = get_object_or_404(WEEMeet, pk=pk)
    if request.user != meet.creater:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form =  WEEMeetForm(request.POST, request.FILES, instance=meet)
        if form.is_valid():
            o = form.save(commit=False)
            o.lesson = meet.lesson
            o.save()
            return HttpResponseRedirect(o.get_absolute_url())
    else:
        form = WEEMeetForm(instance=meet)

    return render(request, 'weemeet/create.html',
            {'form': form,'is_edit': True, 'meet': meet})


@login_required
def delete(request, pk):
    meet = get_object_or_404(WEEMeet, pk=pk)
    if request.user == meet.creater:
        meet.delete()
    else:
        return HttpResponseForbidden()

    return HttpResponseRedirect('/lesson/')

