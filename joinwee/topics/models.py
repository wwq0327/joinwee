# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import fields
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.encoding import force_str

from notifications.signals import notify

class TopicsManager(models.Manager):

    #def in_moderation(self):
    #    """
    #    QuerySet for all comments currently in the moderation queue.
    #    """
    #    return         self.get_queryset().filter(is_public=False, is_removed=False)

    def for_model(self, model):
        """
        QuerySet for all comments for a particular model (either an instance or
        a class).
        """
        ct = ContentType.objects.get_for_model(model)
        qs = self.get_queryset().filter(content_type=ct)
        if isinstance(model, models.Model):
            qs = qs.filter(object_pk=force_str(model._get_pk_val()))
        return qs
    
    def for_object(self, model, pk):
        pass

    def get_user_topic(self, model):
        ct = ContentType.objects.get(app_label=model, model=model)
        qs = self.get_queryset().filter(content_type=ct)

        if model in ['weelesson', 'weemeet']:
            qs = qs.all()

        return qs
    def get_lesson_topic(self):
        return self.get_user_topic(model='weelesson')

    def get_meet_topic(self):
        return self.get_user_topic(model='weemeet')


class Topics(models.Model):
    """
    An abstract base class that any custom comment models probably should
    subclass.
    """

    # Content-object field
    content_type = models.ForeignKey(ContentType,
            on_delete=models.CASCADE,
            verbose_name=_('content type'),
            related_name="content_type_set_for_%(class)s")
    object_pk = models.TextField('object_ID')
    content_object = fields.GenericForeignKey(ct_field="content_type", fk_field="object_pk")

    # Metadata about the comment
    #site = models.ForeignKey(Site)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(u'主题', max_length=128)
    comment = models.TextField(u'内容', max_length=1000, help_text=u'支持makdown语法')
    pub_date = models.DateTimeField(auto_now_add=True)
    
    objects = TopicsManager()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('t_topic', kwargs={'pk': self.pk})

class Reply(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(u'回复内容', max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return f'{self.user.profile.get_nick_name}: {self.content[:30]}'


# 当用户发起一个新的讨论时，系统会自动将一条消息发送给所属微课的作者
def topic_handler(sender, instance, created, **kwargs):
    lesson = instance.content_object
    if instance.user == lesson.creater:
        return 
    notify.send(instance.user,               # 消息发送者
                recipient=lesson.creater,    # 消息接收者
                verb=u'发起了的一个新讨论',     #消息的动作名称
                action_object=lesson,        # 消息产生于对象
                target=instance,             # 产生的目标讨论记录
                public=False
                )
# def topic_del_handler(sender, instance, **kwargs):
#     lesson = instance.content_object
#     topic = instance
#     if lesson:
#         lesson_topic_no = lesson.creater.notifications.filter(target_object_id=topic.id)
    
#     topic_comment_no = topic.user.notifications.filter(action_object_object_id=topic.id)

#     if lesson_topic_no:
#         lesson_topic_no.delete()

#     if topic_comment_no:
#         topic_comment_no.delete()


# 当用户对当前讨论发起新的评论时，系统会自动发送一条消息给讨论发起人
def comment_handler(sender, instance, created, **kwargs):
    topic = instance.content_object
    if topic.user == instance.user:
        return
    notify.send(instance.user,
                recipient=topic.user,
                verb=u'新评论',
                action_object=topic,
                public=False
                )

from django.db.models.signals import post_save, post_delete

post_save.connect(topic_handler, sender=Topics)
#post_save.connect(comment_handler, sender=Comment)
# post_delete.connect(topic_del_handler, sender=Topics)
   
