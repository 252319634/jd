# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_goodsclass_gcl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
