# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-18 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20180918_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='header1',
            field=models.CharField(blank=True, max_length=500, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
    ]