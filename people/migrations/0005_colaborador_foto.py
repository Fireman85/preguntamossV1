# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20170331_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotoscolaboradores'),
        ),
    ]
