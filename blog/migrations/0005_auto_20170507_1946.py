# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170413_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_post',
            field=models.ImageField(blank=True, null=True, upload_to='img_blog', verbose_name='imagen adjunta'),
        ),
    ]
