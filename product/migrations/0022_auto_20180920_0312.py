# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-20 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_product_header_sert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='header_sert',
            field=models.CharField(blank=True, db_index=True, max_length=150, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0431\u043b\u043e\u043a\u0430 \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u044b'),
        ),
    ]