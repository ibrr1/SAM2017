# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0010_auto_20151101_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='is_new_paper',
            field=models.BooleanField(default=True),
        ),
    ]
