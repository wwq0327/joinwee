# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils.encoding import force_text
#from weelesson.models import WEELesson
#from weemeet.models import WEEMeet

class FavManager(models.Manager):

    #def in_moderation(self):
    #    """
    #    QuerySet for all comments currently in the moderation queue.
    #    """
    #    return self.get_query_set().filter(is_public=False, is_removed=False)

    def for_model(self, model):
        """
        QuerySet for all comments for a particular model (either an instance or
        a class).
        """
        ct = ContentType.objects.get_for_model(model)
        qs = self.get_query_set().filter(content_type=ct)
        if isinstance(model, models.Model):
            qs = qs.filter(object_pk=force_text(model._get_pk_val()))
        return qs

    def for_object(self, model, pk):
        pass

    def get_user_fav(self, model):
        '''显示用户收藏的model条目'''
        ct = ContentType.objects.get(app_label=model, model=model)
        qs = self.get_query_set().filter(content_type=ct)

        if model in ['weelesson', 'weemeet']:
            qs = qs.all()

        return qs
    def get_lesson_fav(self):
        '''获得课程的收藏条目'''
        return self.get_user_fav(model='weelesson')

    def get_meet_fav(self):
        '''获得微聚的收藏条目'''
        return self.get_user_fav(model='weemeet')

class Fav(models.Model):
    '''关注或加入微课'''
    content_type = models.ForeignKey(ContentType,
            verbose_name = u'内容类型',
            related_name="content_type_set_for_%(class)s")
    object_pk = models.TextField('object_ID')
    content_object = generic.GenericForeignKey(ct_field="content_type", fk_field="object_pk")

    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True)
    objects = FavManager()

    class Meta:
        ordering = ['-id']


class Join(models.Model):
    '''参与聚会'''
    content_type = models.ForeignKey(ContentType,
            verbose_name=u'内容类型',
            related_name="content_type_set_for_%(class)s")
    object_pk = models.TextField('object_ID')
    content_object = generic.GenericForeignKey(ct_field="content_type", fk_field="object_pk")

    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True)
    objects = FavManager()

    class Meta:
        ordering = ['-id']

