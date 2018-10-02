# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from contact.models import RegularSend
# Register your models here.


class RegularSendAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
admin.site.register(RegularSend, RegularSendAdmin)