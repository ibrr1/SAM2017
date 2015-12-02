# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0033_auto_20151123_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaperDeadLine',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date_deadline', models.DateTimeField(default=datetime.datetime(2015, 11, 30, 14, 6, 44, 703116))),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionChoice',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='notification',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='reviewers',
        ),
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 14, 6, 44, 704117)),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(null=True, to='sam2017_app.User', blank=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 30, 14, 6, 44, 702116)),
        ),
        migrations.AlterField(
            model_name='submission',
            name='reviews',
            field=models.ManyToManyField(to='sam2017_app.Review', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='submissionchoice',
            name='choice',
            field=models.ForeignKey(to='sam2017_app.Submission'),
        ),
        migrations.AddField(
            model_name='submissionchoice',
            name='chooser',
            field=models.ForeignKey(to='sam2017_app.User'),
        ),
    ]
