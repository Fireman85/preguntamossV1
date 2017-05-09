# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-05 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(db_index=True, max_length=50)),
                ('apellidos', models.CharField(db_index=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('es_estudiante', models.BooleanField()),
                ('es_docente', models.BooleanField()),
                ('slug', models.SlugField(max_length=31, unique=True)),
            ],
        ),
    ]