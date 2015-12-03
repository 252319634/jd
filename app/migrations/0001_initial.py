# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('userName', models.CharField(unique=True, max_length=20, db_index=True)),
                ('password', models.CharField(max_length=32)),
                ('registTime', models.DateTimeField(auto_now=True)),
                ('loginTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_user',
            },
        ),
    ]
