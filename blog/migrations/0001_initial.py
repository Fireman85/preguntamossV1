# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0003_auto_20170320_0309'),
        ('question', '0010_auto_20170324_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(help_text='Url de publicación', max_length=63, unique_for_month='pub_date')),
                ('text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='fecha de publicación')),
                ('img_post', models.ImageField(blank=True, upload_to='pic_folder/')),
                ('colaboradores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Colaborador')),
                ('tags', models.ManyToManyField(to='question.Tag')),
            ],
            options={
                'verbose_name': 'Publicaciones',
                'ordering': ['-pub_date', 'title'],
                'get_latest_by': 'pub_date',
            },
        ),
    ]
