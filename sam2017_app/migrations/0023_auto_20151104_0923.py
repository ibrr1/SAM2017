# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0022_auto_20151104_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='review',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='paper',
            field=models.ForeignKey(to='sam2017_app.Paper', null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(to='sam2017_app.User', null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 4, 9, 23, 35, 425167)),
        ),
        migrations.AddField(
            model_name='submission',
            name='paper',
            field=models.ForeignKey(to='sam2017_app.Paper'),
        ),
        migrations.AddField(
            model_name='submission',
            name='review1',
            field=models.ForeignKey(null=True, blank=True, to='sam2017_app.Review', related_name='review1'),
        ),
        migrations.AddField(
            model_name='submission',
            name='review2',
            field=models.ForeignKey(null=True, blank=True, to='sam2017_app.Review', related_name='review2'),
        ),
        migrations.AddField(
            model_name='submission',
            name='review3',
            field=models.ForeignKey(null=True, blank=True, to='sam2017_app.Review', related_name='review3'),
        ),
        migrations.AddField(
            model_name='submission',
            name='reviewer1',
            field=models.ForeignKey(null=True, blank=True, to='sam2017_app.User', related_name='reviewer1'),
        ),
        migrations.AddField(
            model_name='submission',
            name='reviewer2',
            field=models.ForeignKey(null=True, blank=True, to='sam2017_app.User', related_name='reviewer2'),
        ),
        migrations.AddField(
            model_name='submission',
            name='reviewer3',
            field=models.ForeignKey(null=True, blank=True, to='sam2017_app.User', related_name='reviewer3'),
        ),
        migrations.AddField(
            model_name='submission',
            name='submitter',
            field=models.ForeignKey(to='sam2017_app.User', related_name='submitter'),
        ),
    ]
