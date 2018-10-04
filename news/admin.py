# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    class Media:
        js = (
            '/static/tiny_mce/tinymce.min.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )
admin.site.register(News, NewsAdmin)

