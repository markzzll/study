# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-05 23:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20180505_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='click_num',
            new_name='click_nums',
        ),
    ]
