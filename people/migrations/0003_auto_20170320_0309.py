# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20170305_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='slug',
            field=models.SlugField(max_length=31),
        ),
    ]
