# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(verbose_name='\u53d1\u8868\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 14, 17, 34, 350000), verbose_name='\u66f4\u65b0\u65f6\u95f4'),
            preserve_default=False,
        ),
    ]
