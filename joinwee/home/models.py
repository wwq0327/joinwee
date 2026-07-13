# -*- coding: utf-8 -*-
from django.db import models

class First(models.Model):
    email = models.EmailField(u'电子信箱')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.email

