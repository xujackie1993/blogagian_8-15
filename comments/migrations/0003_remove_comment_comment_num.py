# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-31 17:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_comment_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_num',
        ),
    ]
