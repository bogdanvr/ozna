# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
# Create your models here.

class News(models.Model):
	name = models.CharField(max_length = 150, blank = True, verbose_name= "Заголовок новости")
	description = models.TextField(blank = True, verbose_name = "Текст новости")
	image = models.ImageField(blank = True, verbose_name = "Изображение")
	date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name = "Новость"
		verbose_name_plural = "Новости"