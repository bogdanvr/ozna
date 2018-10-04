# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from gear.models import Gear

class GearAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    class Media:
        js = (
            '/static/tiny_mce/tinymce.min.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )
admin.site.register(Gear, GearAdmin)