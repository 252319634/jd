# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_goodsclass_cid'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsclass',
            name='gcl',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe7\xad\x89\xe7\xba\xa7'),
            preserve_default=False,
        ),
    ]
