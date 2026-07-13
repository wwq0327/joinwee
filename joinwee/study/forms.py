from django import forms
from study.models import Study


class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ("number", "content", "start_time", "end_time", "tags",)
