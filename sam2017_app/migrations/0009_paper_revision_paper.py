# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0008_paper_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='revision_paper',
            field=models.CharField(default='No', max_length=30),
            preserve_default=False,
        ),
    ]
