# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from study.models import Study
from study.forms import StudyForm
from weelesson.models import WEELesson
from fav.models import Fav, Join

@login_required
def create(request, pk):
    study_all = request.user.study_set.all()
    lesson = get_object_or_404(WEELesson, pk=pk)
    if study_all:
        this_lesson_study = [s for s in study_all if s.lesson==lesson]
    if request.method == "POST":
        form = StudyForm(request.POST)
        if form.is_valid():
            o = form.save(commit=False)
            o.lesson = lesson
            o.issue = len(this_lesson_study) + 1
            o.creater = request.user
            o.save()

            return HttpResponseRedirect(reverse("study.views.detail", args=(o.pk,)))
    else:
        form = StudyForm()

    return render_to_response('study/create.html',
                              {'form': form},
                              context_instance=RequestContext(request))


def detail(request, pk):
    """研修详情"""

    study = get_object_or_404(Study, pk=pk)
    ct = ContentType.objects.get(app_label='study', model='study')
    try:
        if request.user.is_authenticated():
           fav = request.user.fav_set.get(object_pk=study.pk, content_type=ct)

           if fav:
               is_fav = True
           else:
               is_fav = False
        else:
            is_fav = False
    except Fav.DoesNotExist:
        is_fav = False

    try:
        if request.user.is_authenticated():
            join = request.user.join_set.get(object_pk=study.pk, content_type=ct)
            if join:
                is_join = True
            else:
                is_join = False
        else:
            is_join = False
    except Join.DoesNotExist:
        is_join = False

    #topics = Topics.objects.for_model(meet.lesson) #话题都转到相应的微课上去
    favs = Fav.objects.for_model(study)
    joins = Join.objects.for_model(study)
    point = "%.2f" % (float(joins.count()/float(study.number))*100) #取两位小数
    return render_to_response("study/detail.html",
                              {"study": study,
                               "is_fav": is_fav,
                               "is_join": is_join,
                               "joins": joins,
                               "favs": favs,
                               "point": point},
                              context_instance=RequestContext(request))

@login_required
def edit(request, pk):
    study= get_object_or_404(Study, pk=pk)
    if request.user != study.creater:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form =  StudyForm(request.POST, instance=study)
        if form.is_valid():
            o = form.save(commit=False)
            o.save()
            return HttpResponseRedirect(o.get_absolute_url())
    else:
        form = StudyForm(instance=study)

    return render_to_response('study/create.html',
            {'form': form,'is_edit': True, 'study': study},
            context_instance=RequestContext(request))

