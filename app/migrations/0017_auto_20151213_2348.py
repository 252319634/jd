# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_goodsclass_cid'),
    ]

    operations = [
        migrations.CreateModel(
            name='GCL1',
            fields=[
                ('cid', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('cn', models.CharField(unique=True, max_length=20, verbose_name=b'\xe4\xb8\x80\xe7\xba\xa7\xe7\xb1\xbb\xe5\x90\x8d')),
                ('state', models.SmallIntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x90\xaf\xe7\x94\xa8')),
                ('priority', models.SmallIntegerField(default=1, verbose_name=b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7')),
            ],
            options={
                'db_table': 'tb_gcl1',
            },
        ),
        migrations.CreateModel(
            name='GCL2',
            fields=[
                ('pid', models.SmallIntegerField(verbose_name=b'\xe7\x88\xb6\xe7\xb1\xbbid')),
                ('cid', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('cn', models.CharField(unique=True, max_length=20, verbose_name=b'\xe4\xba\x8c\xe7\xba\xa7\xe7\xb1\xbb\xe5\x90\x8d')),
                ('state', models.SmallIntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x90\xaf\xe7\x94\xa8')),
                ('priority', models.SmallIntegerField(default=1, verbose_name=b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7')),
            ],
            options={
                'db_table': 'tb_gcl2',
            },
        ),
        migrations.CreateModel(
            name='GCL3',
            fields=[
                ('pid', models.SmallIntegerField(verbose_name=b'\xe7\x88\xb6\xe7\xb1\xbbid')),
                ('cid', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('cn', models.CharField(max_length=20, verbose_name=b'\xe7\xb1\xbb\xe5\x90\x8d')),
                ('state', models.SmallIntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x90\xaf\xe7\x94\xa8')),
                ('priority', models.SmallIntegerField(default=1, verbose_name=b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7')),
            ],
            options={
                'db_table': 'tb_gcl3',
            },
        ),
        migrations.DeleteModel(
            name='GoodsClass',
        ),
    ]
