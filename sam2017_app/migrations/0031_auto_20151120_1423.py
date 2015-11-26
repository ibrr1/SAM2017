# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0030_auto_20151117_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reminder',
            old_name='reminderType',
            new_name='reminder_type',
        ),
        migrations.AddField(
            model_name='reminder',
            name='reminder_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='paper',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 14, 23, 24, 707929)),
        ),
    ]
