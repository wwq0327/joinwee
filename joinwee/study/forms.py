#  -*- coding: utf-8 -*-

from django import forms
from study.models import Study

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study

        fields = ("number", "content", "start_time", "end_time", "tags",)

    def save(self, commit=True, force_insert=True, force_update=True):
        return super(StudyForm, self).save(commit=False)
