# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-21 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0030_auto_20180921_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='struktura',
            field=models.ImageField(blank=True, upload_to=b'', verbose_name='\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430 \u0443\u0441\u043b\u043e\u0432\u043d\u043e\u0433\u043e \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f'),
        ),
    ]
