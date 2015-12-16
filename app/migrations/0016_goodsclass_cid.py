# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_goodsclass_gcl'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsclass',
            name='cid',
            field=models.SmallIntegerField(default=1, unique=True, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbbid'),
            preserve_default=False,
        ),
    ]
