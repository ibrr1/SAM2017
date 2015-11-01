# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0006_auto_20151031_0357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='author',
            new_name='submitter',
        ),
    ]
