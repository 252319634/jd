# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20151208_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsclass',
            name='cn',
            field=models.CharField(max_length=20, verbose_name=b'\xe7\xb1\xbb\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='goodsclass',
            name='pid',
            field=models.SmallIntegerField(verbose_name=b'\xe7\x88\xb6\xe7\xba\xa7cid'),
        ),
    ]
