from django import forms
from home.models import First


class FirstForm(forms.ModelForm):
    class Meta:
        model = First
        fields = ('email',)
