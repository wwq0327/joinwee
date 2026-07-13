# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(u'分类名', max_length=12)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(u'标题', max_length=24)
    slug = models.SlugField(u'slug', max_length=36)
    po_type = models.ForeignKey(
        Category, verbose_name=u'文章类型', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    content = models.TextField(u'内容', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post', (), {'slug': self.slug})
