# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField
import datetime, time

from weelesson.models import WEELesson
from weemeet.utils import ch_time

def get_sentinel_lesson():
    user = User.objects.get(pk='-1')
    return WEELesson.objects.get_or_create(creater=user, name=u"微课已被原作者删除")[0]

class WEEMeet(models.Model):
    '''微聚数据'''
    ## name = models.CharField(u'活动名称', max_length=40)
    ## image = ThumbnailerImageField('微聚海报',
    ##         upload_to='uploads/weemeet',
    ##         help_text=u'图片尺寸请不要小于300x300pix')

    ## lesson = models.ForeignKey(WEELesson)
    lesson = models.ForeignKey(WEELesson, on_delete=models.SET(get_sentinel_lesson))
    creater = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    city = models.CharField(u'所在城市', max_length=30,
            help_text=u'如：四川成都')
    address = models.CharField(u'详细地址',
            max_length=24,
            help_text=u'活动详细地址')
    cost = models.CharField(u'费用', blank=True, null=True, max_length=12)
    number = models.IntegerField(u'人数规模', max_length=5,
            help_text=u'人数多少，请只填半角数字')
    summary = models.TextField(u'微聚详情',
            blank=True, null=True,
            help_text=u'使用Markdown语法，说明请点击<a href="http://wowubuntu.com/markdown/" target="_blank">这里</a>')
    start_time = models.DateTimeField(u'开始时间')
    end_time = models.DateTimeField(u'结束时间')

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return 'Meet: %s, Lesson: %s' % (self.pk, self.lesson.name)

    @models.permalink
    def get_absolute_url(self):
        return ('meet_detail', (), {'pk': self.pk})

    def get_time(self):
        state = ['筹备中', '已结束', '进行中']
        now = time.localtime()
        start = ch_time(self.start_time)
        end = ch_time(self.end_time)

        if now < start:
            return state[0]
        elif now > end:
            return state[1]
        else:
            return state[2]

    @property
    def over(self):
        now = time.localtime()
        end = ch_time(self.end_time)
        if now > end:
            return True

        return False
    @property
    def get_stats(self):
        now = time.localtime()
        start = ch_time(self.start_time)
        end = ch_time(self.end_time)

        if now < start:
            return -1
        elif now > end:
            return 1
        else:
            return 0

    @property
    def get_meet_creater_header(self):
        '''获取微聚创建者的个头像
        '''

        if self.creater.profile.mugshot:
            return self.creater.profile.mugshot
        else:
            return self.creater.profile.get_mugshot_url
    @property
    def get_join(self):
        from fav.models import Join
        return Join.objects.for_model(self)

