# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_goodsclass_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsclass',
            name='gcl',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe7\xba\xa7\xe5\x88\xab'),
            preserve_default=False,
        ),
    ]
