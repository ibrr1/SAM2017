# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0012_auto_20151101_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 1, 17, 34, 46, 395561)),
        ),
    ]
