# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from django.urls import reverse

from django.contrib.auth.models import User

from easy_thumbnails.fields import ThumbnailerImageField

#from brands.models import Brands
from topics.models import Topics
from fav.models import Fav
from weelesson.managers import LessonManager
    
class WEELesson(models.Model):
    '''微课models'''
    name = models.CharField(u'微课名称', max_length=128,
                            help_text=u'一个好的名称会是一个良好的开始'
            )
    materials = models.TextField(u'学习内容',
                                 blank=True,
                                 null=True,
                                 help_text=u'使用Markdown语法，说明请点击<a href="http://wowubuntu.com/markdown/" target="_blank">这里</a>')

    #brands = models.ForeignKey(Brands)
    image = ThumbnailerImageField('微课图片',
                                  upload_to='uploads/weelesson',
                                  blank=True,
                                  null=True,
                                  help_text=u'图片尺寸请不要小于300x200px')
    creater = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    desc = models.CharField(u'微课简介',
                            blank=True,
                            null=True,
                            max_length=140,
                            )
    level = models.CharField(u'难度等级',
                             max_length=1,
                             default=1,
                             blank=True,
                             null=True)
    is_fine = models.BooleanField(default=0, blank=True) #是否为精品课程，默认为否，设置需在后台进行
    is_draft = models.BooleanField(u'存为草稿', default=True, blank=True) # 是否存为草稿, 默认为否
    #tags = TaggableManager(blank=True)
    objects = LessonManager()
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return 'Lesson: %s' % self.name

    def get_absolute_url(self):
        return reverse('weelesson_detail', kwargs={'pk': self.pk})

    @property
    def get_pre_lesson(self):
        ## 下篇微课
        _pre = self.__class__.objects.filter(Q(id__lt=self.id), Q(is_draft=False))
        if _pre:
            return _pre[0]
        return False

    @property
    def get_next_lesson(self):
        ## 上篇微课
        _next = self.__class__.objects.filter(Q(id__gt=self.id), Q(is_draft=False)).order_by('id')
        if _next:
            # print _next
            return _next[0]
        return False
        
    @property
    def get_brands(self):
        '''获取该课程的品牌名实例'''
        return None
    @property
    def get_meet(self):
        '''获取本课程的全部微聚'''

        meets = self.weemeet_set.all()
        if meets:
            return meets
        else:
            return ''

    @property
    def get_studies(self):
        studies = self.study_set.all()

        return studies

    @property
    def get_topics(self):
        '''
        获取当前微课下的所有话题
        '''

        topics = Topics.objects.for_model(self)
        return topics

    @property
    def get_favs(self):
        '''
        获取当前微课下的所有参与者
        '''

        return Fav.objects.for_model(self)

class FineLesson(models.Model):
    '''精品微课'''
    lesson = models.OneToOneField(WEELesson, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "FindLesson %s" % self.lesson.name

def get_finelesson_count(user):
    '''获取指定用户的精品课程数量'''
    fls = FineLesson.objects.filter(lesson__creater=user)
    return fls.count()
