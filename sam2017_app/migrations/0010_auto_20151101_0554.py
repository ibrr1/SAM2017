# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0009_paper_revision_paper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(default='Author', choices=[('Author', 'Author'), ('PCM', 'PCM'), ('PCC', 'PCC'), ('admin', 'Admin')], max_length=10),
        ),
    ]
