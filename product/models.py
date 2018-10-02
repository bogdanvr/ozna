# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings




class Category(models.Model):
	name = models.CharField(max_length = 150, verbose_name = "Категория")
	title = models.CharField(max_length = 150, verbose_name = "Название страницы")
	desc = models.CharField(max_length = 300, verbose_name = "Описание")
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name="Категорию"
		verbose_name_plural="Категории"

class Sertifikat(models.Model):
    title = models.CharField(max_length = 150, blank = True, db_index = True, verbose_name = " имя сертификата")
    image = models.ImageField(blank=True, verbose_name = "изображение сертификата")
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name="Изображение сертификата"
        verbose_name_plural="Изображения сертификатов"


class Table(models.Model):
    name = models.CharField(max_length = 300, db_index = True, verbose_name = "Имя поля")
    description = models.CharField(max_length = 300, db_index = True, verbose_name = "Значение")
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name="Таблицу"
        verbose_name_plural="Таблицы"  

class ImageDop(models.Model):
    title = models.CharField(max_length = 150, blank = True, db_index = True, verbose_name = " title изображения")
    image = models.ImageField(blank=True, verbose_name = "Дополнительные изображения")
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name="Дополнительное изображение"
        verbose_name_plural="Дополнительные изображения"

class DopOpisanie(models.Model):
    title = models.CharField(max_length = 150, blank = True, db_index = True, verbose_name = " Имя изображения")
    image = models.ImageField(blank=True, verbose_name = "Изображения общего вида")
    description = models.CharField(max_length = 150, blank = True, db_index = True, verbose_name = "Подпись под изображением")
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name="Описание изображений общего вида"
        verbose_name_plural="Описания изображений общего вида"
    
        
class DopOpisanie2(models.Model):
    title = models.CharField(max_length = 150, blank = True, db_index = True, verbose_name = " Имя дополнительного изображения")
    image = models.ImageField(blank=True, verbose_name = "Дополнительное изображение 2")
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name="Описание к дополнительным изображениям"
        verbose_name_plural="Описания дополнительных изображений"


class ImagePortfolio(models.Model):
    name = models.CharField(blank=True, max_length = 150, db_index = True, verbose_name = " Название изображения")
    image = models.ImageField(verbose_name = "Дополнительные изображения")
    description = models.CharField(blank=True, max_length = 300, db_index = True, verbose_name = "Описание к изображениям примеров раелизации")
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name="Пример реализации"
        verbose_name_plural="Примеры реализации"


    

class Product(models.Model):
    category = models.ForeignKey(Category,default=1, verbose_name = "Выберите категорию товара")	
    name = models.CharField(max_length = 150, unique = True, db_index = True, verbose_name = "Название страницы")
    short_text = models.TextField(max_length = 10000, verbose_name = "Краткое описание", blank=True)
    header1 = models.CharField(max_length = 500, verbose_name = "Описание", blank=True)
    text1 = models.TextField(max_length = 10000, verbose_name = "Текст1", blank=True)
    image = models.ImageField(verbose_name = "Основное изображение")
    oprosnik = models.FileField(upload_to=settings.MEDIA_ROOT, null=True, blank=True, verbose_name = "Ссылка на опросный лист")
    header_struktura = models.CharField(max_length = 150, db_index = True, blank=True, verbose_name = "Заголовок структуры условного обозначения")
    struktura = models.ImageField(blank=True, verbose_name = "Структура условного обозначения")
    header_sert = models.CharField(max_length = 150, db_index = True, blank=True, verbose_name = "Заголовок блока сертификаты")
    sertifikat = models.ManyToManyField(Sertifikat, verbose_name = "Сертификаты", blank=True)
    header2 = models.CharField(max_length = 500, verbose_name = "Технические характеристики", blank=True)
    table = models.ManyToManyField(Table, verbose_name = "Таблица", blank=True)
    header3 = models.CharField(max_length = 500, verbose_name = "Заголовок дополнительных изображений", blank=True)
    image3 = models.ManyToManyField(ImageDop, verbose_name = "Дополнительные изображения", blank=True)
    header3_1 = models.CharField(max_length = 500, verbose_name = "Заголовок дополнительных схем", blank=True)
    image3_1 = models.ManyToManyField(DopOpisanie, verbose_name = "Изображения дополнительных схем", blank=True)
    header3_2 = models.CharField(max_length = 500, verbose_name = "Заголовок дополнительных схем2", blank=True)
    image3_2 = models.ManyToManyField(DopOpisanie2, verbose_name = "Изображения дополнительных схем2", blank=True)
    header4 = models.CharField(blank=True, max_length = 500, verbose_name = "Заголовок примеров реализации")
    image4 = models.ManyToManyField(ImagePortfolio, verbose_name = "Примеры реализации", blank=True)
    alias = models.SlugField(verbose_name='Alias товара')
    def __unicode__(self):
        return self.name
    class Meta:
	    verbose_name="товар"
	    verbose_name_plural="товары"


