# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-21 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_auto_20180921_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=models.CharField(max_length=300, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
    ]
