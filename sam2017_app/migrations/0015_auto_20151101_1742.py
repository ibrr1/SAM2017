# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0014_auto_20151101_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 1, 17, 42, 5, 626559)),
        ),
        migrations.AlterField(
            model_name='paper',
            name='paper',
            field=models.FileField(upload_to='submitted_paper'),
        ),
    ]
