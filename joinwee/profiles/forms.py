# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from userena.utils import get_profile_model, get_user_model
from userena import settings as userena_settings
from userena.models import UserenaSignup
from django import forms

from userena.forms import SignupForm
from .utils import string2py

USERNAME_RE = r'^\S+$'
#USERNAME_RE = r'^[\.\w]+$'

attrs_dict = {'class': 'requeired', 'placeholder':'请使用英文字母或数字符号'}

class BsSignupForm(SignupForm):

    username = forms.RegexField(regex=USERNAME_RE,
            max_length=30,
            widget=forms.TextInput(attrs_dict),
            label=_("Username"),
            error_message={'invalid': _('Username must contain only letters, dots and underscores.')})

    def clean_username(self):
        username = string2py(self.cleaned_data['username'])
        try:
            user = get_user_model().objects.get(username__iexact=username)
        except get_user_model().DoesNotExist:
            pass
        else:
            if userena_settings.USERENA_ACTIVATION_REQUIRED \
                   and UserenaSignup.objects.filter(user__username__iexact=username)\
                   .exclude(activation_key=userena_settings.USERENA_ACTIVATED):
                raise forms.ValidationError(u'本用户已注册但尚未激活，请查检你的注册邮箱并激活')
            raise forms.ValidationError(u'用户名已被注册')

        if username in userena_settings.USERENA_FORBIDDEN_USERNAMES:
            raise forms.ValidationError(u'此用户名被禁使用')
        return username

    def __init__ (self, *args, **kw):
        super(BsSignupForm, self).__init__(*args, **kw)

class SignupFormOnlyEmail(SignupForm):
    def __init__(self, *args, **kwargs):
        super(SignupFormOnlyEmail, self).__init__(*args, **kwargs)
        del self.fields['username']

    def save(self):
        email = self.cleaned_data['email']

        while True:
            try:
                username = email.split('@')[0] # 简单实现，需要完善
            except:
                username = email
            try:
                get_user_model().objects.get(username__iexact=username)
            except get_user_model().DoesNotExist: break
        self.cleaned_data['username'] = username
        return super(SignupFormOnlyEmail, self).save()

class BsEditProfileForm(forms.ModelForm):
    about_me = forms.CharField(label=u'个人宣言',
                               widget=forms.Textarea(
                               attrs={'placeholder':'最多只能输入120个字'}))

    class Meta:
        model = get_profile_model()
        fields = ('nick_name', 'mugshot', 'localtion', 'site', 'about_me',)

    def save(self, force_insert=False, force_update=False, commit=True):
        profile = super(BsEditProfileForm, self).save(commit=commit)
        user = profile.user
        user.save()
        return profile


class NewSocialUserForm(forms.Form):
    ## username = forms.RegexField(regex=USERNAME_RE,
    ##                             max_length=30,
    ##                             widget=forms.TextInput(attrs_dict),
    ##                             label=_("Username"),
    ##                             error_message={'invalid': _('Username must contain only letters, dots and underscores.')})

    email = forms.EmailField(label=u'电子邮箱')
    password1 = forms.CharField(label=u'设置密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'重复密码', widget=forms.PasswordInput)

    ## def clean_username(self):

    ##     try:
    ##         user = get_user_model().objects.get(username__iexact=self.cleaned_data['username'])
    ##     except get_user_model().DoesNotExist:
    ##         pass
    ##     else:
    ##         if userena_settings.USERENA_ACTIVATION_REQUIRED \
    ##                and UserenaSignup.objects.filter(user__username__iexact=self.cleaned_data['username'])\
    ##                .exclude(activation_key=userena_settings.USERENA_ACTIVATED):
    ##             raise forms.ValidationError(_('This username is already taken but not confirmed. Please check your email for verification steps.'))
    ##         raise forms.ValidationError(_('This username is already taken.'))
        
    ##     if self.cleaned_data['username'].lower() in userena_settings.USERENA_FORBIDDEN_USERNAMES:
    ##         raise forms.ValidationError(_('This username is not allowed.'))
    ##     return self.cleaned_data['username']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        
        if get_user_model().objects.filter(email__iexact=email):
            raise forms.ValidationError(_('This email is already in use. Please supply a different email.'))

        return email
    
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_('The two password fields didn\'t match.'))
        return self.cleaned_data
