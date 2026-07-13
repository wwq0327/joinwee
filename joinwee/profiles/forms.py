# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from profiles.models import Profile
from .utils import string2py

attrs_dict = {'class': 'requeired', 'placeholder': '请使用英文字母或数字符号'}

class WeeSignupForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs_dict),
        label=_("Username"),
    )

    def clean_username(self):
        username = string2py(self.cleaned_data['username'])
        User = get_user_model()
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(u'用户名已被注册')
        return username

    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.save()

class SignupFormOnlyEmail(forms.Form):
    email = forms.EmailField(label=u'电子邮箱')
    password1 = forms.CharField(label=u'设置密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'重复密码', widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        User = get_user_model()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(_('This email is already in use. Please supply a different email.'))
        return email

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_('The two password fields didn\'t match.'))
        return self.cleaned_data

class BsEditProfileForm(forms.ModelForm):
    about_me = forms.CharField(label=u'个人宣言',
                               widget=forms.Textarea(
                               attrs={'placeholder': '最多只能输入120个字'}))

    class Meta:
        model = Profile
        fields = ('nick_name', 'mugshot', 'localtion', 'site', 'about_me',)

class NewSocialUserForm(forms.Form):
    email = forms.EmailField(label=u'电子邮箱')
    password1 = forms.CharField(label=u'设置密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'重复密码', widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        User = get_user_model()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(_('This email is already in use. Please supply a different email.'))
        return email

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_('The two password fields didn\'t match.'))
        return self.cleaned_data
