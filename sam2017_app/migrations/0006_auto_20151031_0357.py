# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0005_notification_paper_reminder_report_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='owner',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='contact',
            new_name='author_contact',
        ),
        migrations.AddField(
            model_name='paper',
            name='authors_list',
            field=models.CharField(default='ibrahim', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paper',
            name='paper_format',
            field=models.CharField(default='fsdffds', max_length=30),
            preserve_default=False,
        ),
    ]
