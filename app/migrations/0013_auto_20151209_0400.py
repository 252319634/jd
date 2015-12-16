# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20151209_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsclass',
            name='state',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x90\xaf\xe7\x94\xa8'),
        ),
    ]
