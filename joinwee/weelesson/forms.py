#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-26 08:16:51

from django import forms
# from pagedown.widgets import PagedownWidget
#from taggit.forms import TagWidget, TagField
# from epiceditor.widgets import AdminEpicEditorWidget

from weelesson.models import WEELesson

class TitleLessonForm(forms.ModelForm):
    '''只含有标题及内容的Lesson Form，其中标题为必须的，而内容则可有可无
    '''

    materials = forms.CharField(label=u"微课详情", widget=forms.Textarea(attrs={"style":"display:none"}))

    class Meta:
        model = WEELesson
        fields = ('name', 'materials', )
        
    def save(self, commit=True, force_insert=False, force_update=True):

        return super(TitleLessonForm, self).save(commit=False)
    
class WEELessonForm(forms.ModelForm):
    LEVEL = (
        (1, '新手上路'),
        (2, '中级进阶'),
        (3, '高手切磋'),
        (4, '适合所有读者'),
        )

    #materials = forms.CharField(label=u'微课详情',widget=PagedownWidget())
    #tags = TagField(label=u'标签, 请用半角逗号分开', help_text=u'请用半角逗号分开', required=False)
    desc = forms.CharField(label=u'微课简介', widget=forms.Textarea(attrs={'rows':'5'}), required=True, help_text=u'请用140字以内介绍下你的微课')
    image = forms.ImageField(required=True)
    level = forms.TypedChoiceField(label=u"学习难度",
        choices=LEVEL, widget=forms.RadioSelect, coerce=int
        )
    class Meta:
        model = WEELesson
        fields = ('image', 'desc', 'level', )

    def save(self, commit=True, force_insert=False, force_update=True):
    
        return super(WEELessonForm, self).save(commit=False)
