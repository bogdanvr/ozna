# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RegularSend(models.Model):
    name = models.CharField(max_length = 20, verbose_name = "Пользователь")
    email = models.EmailField(verbose_name = "E-mail")
  
    class Meta:
        verbose_name="Подписку"
        verbose_name_plural="Подписки"
