# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0015_auto_20151101_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='is_new_paper',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='submitter',
        ),
        migrations.AlterField(
            model_name='paper',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 3, 20, 9, 41, 523302)),
        ),
        migrations.AlterField(
            model_name='paper',
            name='revision_paper',
            field=models.BooleanField(default=False),
        ),
    ]
