# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.CharField(unique=True, max_length=30, db_index=True),
        ),
    ]
