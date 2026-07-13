# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField

class Brands(models.Model):
    '''品牌model'''
    name = models.CharField(u'品牌名', 
            max_length=120,
            unique=True, #品牌标识唯一
            help_text=u'个人或组织机构品牌名称'
            )
    logo = ThumbnailerImageField(u'品牌LOGO',
            upload_to='uploads/brands',
            help_text=u'请查看相LOGO制作要求')
    created = models.DateTimeField(auto_now_add=True)
    creater = models.ForeignKey(User)
    summary = models.TextField(u'品牌简介', blank=True, null=True)
    active = models.BooleanField(default=0)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('brands_detail', (), {'pk': self.pk})


