# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-14 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AlterField(
            model_name='product',
            name='header2',
            field=models.CharField(blank=True, max_length=500, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='text1',
            field=models.TextField(blank=True, max_length=10000, verbose_name='\u0422\u0435\u043a\u0441\u04421'),
        ),
    ]
