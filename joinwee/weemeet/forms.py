from django import forms
from weemeet.models import WEEMeet


class WEEMeetForm(forms.ModelForm):
    class Meta:
        model = WEEMeet
        fields = ('city', 'address', 'start_time', 'end_time', 'cost', 'number', 'summary',)

    def clean_number(self):
        number = self.cleaned_data['number']
        if number <= 0 and isinstance(number, int):
            raise forms.ValidationError(u'数字必须为大于0的整数')
        return number
