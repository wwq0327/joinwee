#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-23 20:38:06

from django import forms
from home.models import First

class FirstForm(forms.ModelForm):
    class Meta:
        model = First
        fields = ('email',)

    def save(self, commit=True, force_insert=False, force_update=True):
        return super(FirstForm, self).save(commit=False)

