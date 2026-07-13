# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaLanguageBaseProfile
from django.utils.translation import ugettext_lazy as _

#from .utils import string2py

class Profile(UserenaLanguageBaseProfile):
    """Default profile"""

    #SEX_CHOICES=(
    #    (1, u'男'),
    #    (2, u'女'),
    #    )
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name='user',
                                related_name='profile')
    nick_name = models.CharField(u'昵称',
                                max_length=64,
                                unique=True,
                                blank=True,
                                null=True,
                                help_text=u'你的常用网络ID等'
                                )

    localtion = models.CharField(u'来自', max_length=24, blank=True)
    site = models.CharField(u'个人网址', max_length=120, blank=True)
    about_me = models.CharField(u'关于我', max_length=120, blank=True,
                                help_text=u"请不要超过120字")

    def __unicode__(self):
        return self.user.username

    @property
    def get_nick_name(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.user.username

    @property
    def get_user_lessons(self):
        '''如果浏览用户不是当前个人信息页面所属用户，
        则只显示已发布的，对于草稿内容，则不显示
        '''
        return self.user.weelesson_set.published()

class ConfirEmail(models.Model):
    user = models.ForeignKey(User)
    email_confirmation_key = models.CharField(_('unconfirmed email verification key'),
                                              max_length=40,
                                              blank=True)

    email_confirmation_key_created = models.DateTimeField(_('creation date of email confirmation key'),
                                                          blank=True,
                                                          null=True)

    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username
