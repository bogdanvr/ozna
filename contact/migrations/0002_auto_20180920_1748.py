# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-20 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regularsend',
            old_name='content',
            new_name='email',
        ),
    ]
