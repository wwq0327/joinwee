# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

from django.contrib import comments
from django.contrib.comments.views.moderation import perform_delete

from topics.models import Topics
from topics.forms import TopicsForm

def all(request, pk):
    app = 'weelesson'
    ct = ContentType.objects.get(app_label=app, model=app)# 获取类名
    m = ct.get_object_for_this_type(pk=pk) #得到相应的数据
    topics = Topics.objects.for_model(m) # 反相本课程下的讨论话题

    return render_to_response('topics/all.html',
                              {'topics': topics, 'lesson': m},
                              context_instance=RequestContext(request))

@login_required
def create(request, app, pk):
    app = 'wee'+str(app)
    ct = ContentType.objects.get(app_label=app, model=app)# 获取类名
    m = ct.get_object_for_this_type(pk=pk) #得到相应的数据
    if request.method == 'POST':
        form = TopicsForm(request.POST)
        if form.is_valid():
            o = form.save(commit=False)
            o.content_object = m
            o.user = request.user
            o.save()

            return HttpResponseRedirect(o.get_absolute_url())
    else:
        form = TopicsForm()

    return render_to_response('topics/create.html',
            {'form': form, 'm': m},
            context_instance=RequestContext(request))

@login_required
def edit(request, pk):
    #app = 'wee'+str(app)
    #ct = ContentType.objects.get(app_label=app, model=app)# 获取类名
    #m = ct.get_object_for_this_type(pk=pk) #得到相应的数据
    m = get_object_or_404(Topics, pk=pk)
    #m = Topics.objects.get(pk=pk)
    if request.method == 'POST':
        form = TopicsForm(request.POST, instance=m)
        if form.is_valid():
            o = form.save(commit=False)
            o.save()

            return HttpResponseRedirect(o.get_absolute_url())
    else:
        form = TopicsForm(instance=m)

    return render_to_response('topics/create.html',
            {'form': form, 'm': m, 'is_edit': True},
            context_instance=RequestContext(request))

def topic(request, pk):
    t = get_object_or_404(Topics, pk=pk)
    lesson = t.content_object
    #print lesson
    ## 判断微课是否存在，如果存在，则显示微课的其它讨论，否则返回None
    if lesson:
        other_topics = lesson.get_topics.filter(~Q(pk=pk))
    else:
        other_topics = None
    #print other_topics
    
    return render_to_response('topics/topic.html',
            {'t': t,
             'other_topics': other_topics,
             'lesson': lesson,
             },
            context_instance=RequestContext(request))

@login_required    
def delete(request, pk):
    t = get_object_or_404(Topics, pk=pk)
    if t:
        if t.content_object: #如果微课存在
            ## 转到相应微课
            lesson_url = t.content_object.get_absolute_url()
        else:
            ## 转到微课首页面
            lesson_url = '/lesson/'
            
    if request.user == t.user:
        t.delete()
    else:
        return HttpResponseForbidden()
    
    return HttpResponseRedirect(lesson_url)

@login_required
def delete_comment(request, pk):
	comment = get_object_or_404(comments.get_model(), pk=pk)
	next = comment.content_object.get_absolute_url()
	if comment.user != request.user:
		raise Http404
	perform_delete(request, comment)

	return HttpResponseRedirect(next)
	
