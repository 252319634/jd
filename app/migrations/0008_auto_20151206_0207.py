# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsClass',
            fields=[
                ('classID', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('classL1', models.SmallIntegerField(unique=True, null=True, verbose_name=b'\xe4\xb8\x80\xe7\xba\xa7\xe5\x88\x86\xe7\xb1\xbb')),
                ('classL2', models.SmallIntegerField(unique=True, null=True, verbose_name=b'\xe4\xba\x8c\xe7\xba\xa7\xe5\x88\x86\xe7\xb1\xbb')),
                ('classL3', models.SmallIntegerField(unique=True, null=True, verbose_name=b'\xe4\xb8\x89\xe7\xba\xa7\xe5\x88\x86\xe7\xb1\xbb')),
                ('className', models.CharField(unique=True, max_length=20, verbose_name=b'\xe7\xb1\xbb\xe5\x90\x8d')),
            ],
            options={
                'db_table': 'tb_goodsclass',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='classID',
            field=models.SmallIntegerField(default=0, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb'),
            preserve_default=False,
        ),
    ]
