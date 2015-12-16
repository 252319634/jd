# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20151208_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsclass',
            name='priority',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7'),
        ),
    ]
