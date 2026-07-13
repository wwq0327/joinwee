# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from study.models import Study
from study.forms import StudyForm
from weelesson.models import WEELesson
from fav.models import Fav, Join


@login_required
def create(request, pk):
    lesson = get_object_or_404(WEELesson, pk=pk)
    study_all = request.user.study_set.all()
    this_lesson_study = [s for s in study_all if s.lesson == lesson]
    if request.method == "POST":
        form = StudyForm(request.POST)
        if form.is_valid():
            o = form.save(commit=False)
            o.lesson = lesson
            o.issue = len(this_lesson_study) + 1
            o.creater = request.user
            o.save()

            return HttpResponseRedirect(reverse('study_detail', args=(o.pk,)))
    else:
        form = StudyForm()

    return render(request, 'study/create.html',
                              {'form': form})


def detail(request, pk):
    """研修详情"""

    study = get_object_or_404(Study, pk=pk)
    ct = ContentType.objects.get(app_label='study', model='study')
    try:
        if request.user.is_authenticated:
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
        if request.user.is_authenticated:
            join = request.user.join_set.get(object_pk=study.pk, content_type=ct)
            if join:
                is_join = True
            else:
                is_join = False
        else:
            is_join = False
    except Join.DoesNotExist:
        is_join = False

    favs = Fav.objects.for_model(study)
    joins = Join.objects.for_model(study)
    point = "%.2f" % (float(joins.count()/float(study.number))*100)
    return render(request, "study/detail.html",
                              {"study": study,
                               "is_fav": is_fav,
                               "is_join": is_join,
                               "joins": joins,
                               "favs": favs,
                               "point": point})

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

    return render(request, 'study/create.html',
            {'form': form,'is_edit': True, 'study': study})
