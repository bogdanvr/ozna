# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-17 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20180917_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='odnolineyka',
            field=models.FilePathField(default='', path='/home/c/cn68880/django_1/public_html/static/images', verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0443 \u043e\u0434\u043d\u043e\u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0439 \u0441\u0445\u0435\u043c\u044b'),
            preserve_default=False,
        ),
    ]
