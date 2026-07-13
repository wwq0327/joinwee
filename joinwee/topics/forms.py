#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-28 21:53:25

from django import forms
from topics.models import Topics

from pagedown.widgets import PagedownWidget

class TopicsForm(forms.ModelForm):
    comment = forms.CharField(label=u"内容", widget=forms.Textarea(attrs={'rows':'18'}), required=False)
    
    class Meta:
        model = Topics
        fields = ('title', 'comment',)

    def save(self, commit=True, force_insert=True, force_update=True):
        return super(TopicsForm, self).save(commit=False)

