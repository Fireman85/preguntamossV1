# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-24 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0009_auto_20170321_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='img_issue',
            field=models.ImageField(blank=True, upload_to='pic_folder/'),
        ),
    ]
