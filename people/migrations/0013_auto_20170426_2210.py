# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 03:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0012_auto_20170426_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaborador',
            name='link_facebook',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='link_twitter',
        ),
    ]
