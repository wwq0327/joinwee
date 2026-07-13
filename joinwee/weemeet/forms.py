#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-27 18:56:08

from django import forms
from weemeet.models import WEEMeet

class WEEMeetForm(forms.ModelForm):
    class Meta:
        model = WEEMeet
        #fields = ('name', 'image', 'city', 'address', 'start_time', 'end_time', 'cost', 'number', 'summary',)
        fields = ('city', 'address', 'start_time', 'end_time', 'cost', 'number', 'summary',)

    def save(self, commit=True, force_insert=True, force_update=True):
        return super(WEEMeetForm, self).save(commit=False)

    def clean_number(self):
        number = self.cleaned_data['number']
        if number <= 0 and isinstance(number, int):
            raise forms.ValidationError(u'数字必须为大于0的整数')
        return number

