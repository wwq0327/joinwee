from django import forms
from topics.models import Topics


class TopicsForm(forms.ModelForm):
    comment = forms.CharField(label=u"内容", widget=forms.Textarea(attrs={'rows':'18'}), required=False)

    class Meta:
        model = Topics
        fields = ('title', 'comment',)
