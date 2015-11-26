# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0032_update_reminders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(related_name='notifications', null=True, default=None, to='sam2017_app.User'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 23, 14, 45, 33, 435166)),
        ),
    ]
