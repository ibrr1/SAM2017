# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0007_auto_20151031_0547'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
