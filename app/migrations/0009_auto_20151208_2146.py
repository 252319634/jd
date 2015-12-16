# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20151206_0207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodsclass',
            old_name='className',
            new_name='cn',
        ),
        migrations.RenameField(
            model_name='goodsclass',
            old_name='classID',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='goodsclass',
            name='classL1',
        ),
        migrations.RemoveField(
            model_name='goodsclass',
            name='classL2',
        ),
        migrations.RemoveField(
            model_name='goodsclass',
            name='classL3',
        ),
        migrations.AddField(
            model_name='goodsclass',
            name='cid',
            field=models.SmallIntegerField(default=0, unique=True, verbose_name=b'id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goodsclass',
            name='pid',
            field=models.SmallIntegerField(default=0, unique=True, verbose_name=b'\xe7\x88\xb6\xe7\xba\xa7cid'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goodsclass',
            name='priority',
            field=models.SmallIntegerField(default=0, verbose_name=b'\xe4\xbc\x98\xe5\x85\x88\xe7\xba\xa7'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goodsclass',
            name='state',
            field=models.BooleanField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x90\xaf\xe7\x94\xa8'),
            preserve_default=False,
        ),
    ]
