# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from product.models import Product, Table, ImageDop, DopOpisanie, ImagePortfolio, Category, DopOpisanie2, Sertifikat

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_text')
    class Media:
        js = (
            '/static/tiny_mce/tinymce.min.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )
admin.site.register(Product, ProductAdmin)

class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
admin.site.register(Table, TableAdmin)

class ImageDopAdmin(admin.ModelAdmin):
    list_display = ('image', 'title')
admin.site.register(ImageDop, ImageDopAdmin)

class ImagePortfolioAdmin(admin.ModelAdmin):
    list_display = ('name' ,'image', 'description')
admin.site.register(ImagePortfolio, ImagePortfolioAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category, CategoryAdmin)

class DopOpisanieAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
admin.site.register(DopOpisanie, DopOpisanieAdmin)

class DopOpisanie2Admin(admin.ModelAdmin):
    list_display = ('title', 'image')
admin.site.register(DopOpisanie2, DopOpisanie2Admin)

class SertifikatAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
admin.site.register(Sertifikat, SertifikatAdmin)