# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Gear(models.Model):
	name = models.CharField(max_length = 150, verbose_name = "Название оборудования")
	image = models.ImageField(blank = True, verbose_name = "Изображение оборудования")
	description = models.TextField(blank = True, verbose_name = "Описание оборудования")
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name="Оборудование"
		verbose_name_plural="Оборудование"