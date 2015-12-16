# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20151213_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsClass',
            fields=[
                ('pid', models.SmallIntegerField(default=0, verbose_name=b'\xe7\x88\xb6\xe7\xba\xa7\xe5\x88\x86\xe7\xb1\xbbid')),
                ('cid', models.AutoField(unique=True, serialize=False, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbbid', primary_key=True)),
                ('cn', models.CharField(unique=True, max_length=20, verbose_name=b'\xe4\xb8\x80\xe7\xba\xa7\xe7\xb1\xbb\xe5\x90\x8d')),
                ('state', models.SmallIntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x90\xaf\xe7\x94\xa8')),
                ('priority', models.SmallIntegerField(default=1, verbose_name=b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7')),
            ],
            options={
                'db_table': 'tb_goodsclass',
            },
        ),
        migrations.DeleteModel(
            name='GCL1',
        ),
        migrations.DeleteModel(
            name='GCL2',
        ),
        migrations.DeleteModel(
            name='GCL3',
        ),
    ]
