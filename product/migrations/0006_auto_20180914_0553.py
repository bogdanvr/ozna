# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-14 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20180914_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='header3',
            field=models.CharField(blank=True, max_length=500, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439'),
        ),
    ]
