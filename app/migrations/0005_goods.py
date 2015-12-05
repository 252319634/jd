# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('goodsID', models.AutoField(unique=True, serialize=False, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xbc\x96\xe5\x8f\xb7', primary_key=True)),
                ('goodsName', models.CharField(unique=True, max_length=30, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0', db_index=True)),
                ('dingjia', models.FloatField(verbose_name=b'\xe5\xae\x9a\xe4\xbb\xb7')),
                ('bendianjia', models.FloatField(verbose_name=b'\xe6\x9c\xac\xe5\xba\x97\xe4\xbb\xb7')),
                ('shangjiashijian', models.DateField(auto_now=True, verbose_name=b'\xe4\xb8\x8a\xe6\x9e\xb6\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'tb_goods',
            },
        ),
    ]
