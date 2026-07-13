# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.csrf import csrf_exempt

from weelesson.models import WEELesson
from weelesson.forms import WEELessonForm, TitleLessonForm
from topics.models import Topics
from fav.models import Fav

from hitcount.models import HitCount

def index(request):
    '''微课首页面'''

    if request.GET.get('order', '') == 'featured':
        #lessons = get_list_or_404(WEELesson, is_fine=True, is_draft=False)
        lessons = WEELesson.objects.published().fine()
    elif request.GET.get('order', '') == 'hit':
        ct = ContentType.objects.get(app_label='weelesson', model='weelesson')
        hits = HitCount.objects.filter(content_type=ct)
        lessons = [h.content_object for h in hits if h.content_object.is_draft==False]

    elif request.GET.get('level', ''):
         _level = request.GET.get('level', '')
         lessons = WEELesson.objects.published().filter(level=_level)
    else:
        lessons = WEELesson.objects.published()

    return render_to_response('weelesson/index.html',
            {'lessons': lessons},
            context_instance=RequestContext(request))

def draft(request, pk):
    lesson = get_object_or_404(WEELesson, pk=pk)
    if lesson.creater != request.user or lesson.is_draft == False: ## 微课非创建者本人，或是微课已是发布状态，则404
        raise Http404()
        
    return render_to_response('weelesson/draft.html',
                              {'lesson':lesson},
                              context_instance=RequestContext(request))

def level(request):
    '''微课不同难度等级的显示'''
    _level = request.GET.get('level', '')
    ## _lessons = get_list_or_404(WEELesson, is_draft=False)

    ## lessons = _lessons.filter(level=_level) # 等级为4
    lessons = WEELesson.objects.published().filter(level=_level)
    return render_to_response('weelesson/index.html',
            {'lessons': lessons},
            context_instance=RequestContext(request))

def lesson(request, pk):
   '''微课页面'''

   lesson = get_object_or_404(WEELesson, pk=pk)

   if lesson.is_draft == True and request.user != lesson.creater:
       raise Http404()

   if request.GET.get('m', '') == 'full-reader':
       return render_to_response('weelesson/full-read.html',
                                 {'lesson': lesson,},
                                 context_instance=RequestContext(request))

   meets = lesson.weemeet_set.all() #得到前两个活动 可能有BUG
   topics = Topics.objects.for_model(lesson) # 反相本课程下的讨论话题
   studies = lesson.study_set.all()
   ct = ContentType.objects.get(app_label='weelesson', model='weelesson')
   try:
       if request.user.is_authenticated():
           fav = request.user.fav_set.get(object_pk=lesson.pk, content_type=ct)
           if fav:
               is_fav = True
           else:
               is_fav = False
       else:
           is_fav = False
   except Fav.DoesNotExist:
       is_fav = False

   favs = Fav.objects.for_model(lesson)

   return render_to_response('weelesson/lesson.html',
           {'lesson': lesson, 'topics': topics, 'meets': meets, 'is_fav': is_fav, 'favs': favs, "studies": studies},
           context_instance=RequestContext(request))

@login_required
@csrf_exempt
def create(request):
    '''编辑一个草稿'''
    
    lesson = WEELesson.objects.create(name=u'无标题微课', creater=request.user)

    if request.is_ajax():
        _name = request.POST.get('name', '')
        _materials = request.POST.get('materials', '')
        if _name:
            lesson.name = _name
            lesson.materials = _materials
            lesson.save()
            msg = u"保存成功！"
        else:
            msg = u"缺少标题!"


        return HttpResponse(msg)
    else:
        form = TitleLessonForm(instance=lesson)
        
    return render_to_response('weelesson/create.html',
                              {'form': form,
                               'is_edit': False,
                               'lesson':lesson},
                              context_instance=RequestContext(request))

@login_required
def info(request, pk):
    '''填微课周边信息'''
    lesson = get_object_or_404(WEELesson, pk=pk)
    if lesson.is_draft == True:
        is_edit = False
    else: is_edit = True
        
    if request.method == 'POST':
        form = WEELessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            o = form.save(commit=False)
            ## o.creater = request.user
            ## o.name = lesson.name
            ## o.materials = lesson.materials
            ## o.is_draft = False
            o.save()

            return HttpResponseRedirect(reverse('weelesson.views.info', args=(o.pk,)))
    else:
        form = WEELessonForm(instance=lesson)

    return render_to_response('weelesson/info.html',
            {'form': form,
             'lesson': lesson,
             'is_edit': is_edit
             },
            context_instance=RequestContext(request))

@login_required
def publish(request, pk):
  '''发布微课'''

  lesson = get_object_or_404(WEELesson, pk=pk)
  if lesson.creater == request.user:
      lesson.is_draft = False
      lesson.save()
  else:
      raise Http404()

  return HttpResponseRedirect(reverse('weelesson.views.lesson', args=(lesson.pk, )))

@login_required
def unpublish(request, pk):
    lesson = get_object_or_404(WEELesson, pk=pk)
    if lesson.creater == request.user:
        lesson.is_draft = True
        lesson.save()
    else:
        raise Http404()

    return HttpResponseRedirect(reverse('le_mg', args=(request.user, )))

@login_required
@csrf_exempt
def edit(request, pk):
    '''编辑一个草稿'''
    
    lesson = get_object_or_404(WEELesson, pk=pk)
    if request.user != lesson.creater:
        return HttpResponseForbidden()

    if request.is_ajax():
        _name = request.POST.get('name', '')
        _materials = request.POST.get('materials', '')
        if _name:
            lesson.name = _name
            lesson.materials = _materials
            lesson.save()
            msg = u"保存成功！"
        else:
            msg = u"缺少标题!"

        return HttpResponse(msg)
    else:
        form = TitleLessonForm(instance=lesson)
        
    return render_to_response('weelesson/create.html',
                              {'form': form,
                               'is_edit': True,
                               'lesson':lesson},
                              context_instance=RequestContext(request))

@login_required
def delete(request, pk):
    lesson = get_object_or_404(WEELesson, pk=pk)
    if request.user == lesson.creater:
        lesson.delete()
    else:
        return HttpResponseForbidden()

    return HttpResponseRedirect(reverse('profiles.views.manager_lesson', args=(request.user.username,)))

