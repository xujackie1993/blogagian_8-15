# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-31 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name=b'\xe9\x98\x85\xe8\xaf\xbb'),
        ),
    ]
