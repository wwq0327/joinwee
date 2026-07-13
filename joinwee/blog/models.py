# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class BlogComment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(u'评论内容', max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return f'{self.user.profile.get_nick_name}: {self.content[:30]}'


class Category(models.Model):
    name = models.CharField(u'分类名', max_length=12)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(u'标题', max_length=24)
    slug = models.SlugField(u'slug', max_length=36)
    po_type = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name=u'文章类型', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(u'内容', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'slug': self.slug})
