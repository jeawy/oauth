# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-06 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='head_portrait',
            field=models.ImageField(default='/media/portrait/no_img/no_portrait1.jpg', upload_to='portrait', verbose_name='选择头像'),
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='thumbnail_portait',
            field=models.ImageField(default='/media/portrait/no_img/no_portrait1.jpg', upload_to='portrait', verbose_name='头像缩略图'),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='type',
            field=models.CharField(default='0', max_length=5, verbose_name='type'),
        ),
    ]
