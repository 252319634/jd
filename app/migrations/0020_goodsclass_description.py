# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20151214_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsclass',
            name='description',
            field=models.TextField(default='', verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab\xe6\x8f\x8f\xe8\xbf\xb0'),
            preserve_default=False,
        ),
    ]
