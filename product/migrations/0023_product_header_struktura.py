# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-20 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_auto_20180920_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='header_struktura',
            field=models.CharField(db_index=True, default=' ', max_length=150, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u044b \u0443\u0441\u043b\u043e\u0432\u043d\u043e\u0433\u043e \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f'),
            preserve_default=False,
        ),
    ]
