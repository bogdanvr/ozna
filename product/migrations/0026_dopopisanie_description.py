# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-20 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_auto_20180920_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='dopopisanie',
            name='description',
            field=models.CharField(blank=True, db_index=True, max_length=50, verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u044c \u043f\u043e\u0434 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435\u043c'),
        ),
    ]