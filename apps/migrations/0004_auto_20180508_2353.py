# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-08 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20180107_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtoken',
            name='token',
            field=models.CharField(max_length=128),
        ),
    ]
