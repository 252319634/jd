# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20151214_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsclass',
            name='cn',
            field=models.CharField(max_length=20, verbose_name=b'\xe4\xb8\x80\xe7\xba\xa7\xe7\xb1\xbb\xe5\x90\x8d'),
        ),
    ]
