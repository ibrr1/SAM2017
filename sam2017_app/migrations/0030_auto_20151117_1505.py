# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0029_auto_20151116_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='notificationType',
            new_name='notification_type',
        ),
        migrations.AlterField(
            model_name='paper',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 17, 15, 4, 40, 96775)),
        ),
    ]
