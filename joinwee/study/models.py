# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from weelesson.models import WEELesson

class Study(models.Model):
    """微课研修模型"""
    
    lesson = models.ForeignKey(WEELesson) #, on_delete=models.SET(get_sentinel_lesson))
    creater = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    number = models.IntegerField(u'人数规模', max_length=5)
    issue = models.IntegerField(u'期号',
                                max_length=2,
                                blank=True,
                                null=True,
                                help_text=u"研修期号，如果来研修只做一期，则不必填写")
    content = models.TextField(u'研修详情', blank=True, null=True)
    start_time = models.DateTimeField(u'开始时间')
    end_time = models.DateTimeField(u'结束时间')
    tags = models.CharField(u'传播标签', max_length=24, blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.lesson.name
        
    @models.permalink
    def get_absolute_url(self):
        return ('study_detail', (), {'pk': self.pk})

    @property
    def get_join(self):
        from fav.models import Join
        return Join.objects.for_model(self)
