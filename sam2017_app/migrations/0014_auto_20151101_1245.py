# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0013_auto_20151101_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]
