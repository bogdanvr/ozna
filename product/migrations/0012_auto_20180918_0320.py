# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-18 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20180918_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='oprosnik',
            field=models.FilePathField(path=b'home/c/cn68880/django_1/public_html/media/', verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043e\u043f\u0440\u043e\u0441\u043d\u044b\u0439 \u043b\u0438\u0441\u0442'),
        ),
    ]