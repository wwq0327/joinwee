from django import forms

from weelesson.models import WEELesson


class TitleLessonForm(forms.ModelForm):
    materials = forms.CharField(label=u"微课详情", widget=forms.Textarea(attrs={"style":"display:none"}))

    class Meta:
        model = WEELesson
        fields = ('name', 'materials', )


class WEELessonForm(forms.ModelForm):
    LEVEL = (
        (1, '新手上路'),
        (2, '中级进阶'),
        (3, '高手切磋'),
        (4, '适合所有读者'),
    )

    desc = forms.CharField(label=u'微课简介', widget=forms.Textarea(attrs={'rows':'5'}), required=True, help_text=u'请用140字以内介绍下你的微课')
    image = forms.ImageField(required=True)
    level = forms.TypedChoiceField(label=u"学习难度",
        choices=LEVEL, widget=forms.RadioSelect, coerce=int
    )

    class Meta:
        model = WEELesson
        fields = ('image', 'desc', 'level', )
