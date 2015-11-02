# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0011_paper_is_new_paper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='is_new_paper',
            field=models.BooleanField(default=False),
        ),
    ]
