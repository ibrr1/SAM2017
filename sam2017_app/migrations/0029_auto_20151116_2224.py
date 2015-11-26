# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sam2017_app', '0028_auto_20151104_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='reviewer',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='review1',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='review2',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='review3',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='reviewer1',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='reviewer2',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='reviewer3',
        ),
        migrations.AddField(
            model_name='notification',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='notification',
            name='notificationType',
            field=models.CharField(default='', max_length=127),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(related_name='notifications', to='sam2017_app.User', default=None),
        ),
        migrations.AddField(
            model_name='notification',
            name='viewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reminder',
            name='notification',
            field=models.OneToOneField(to='sam2017_app.Notification', default=None),
        ),
        migrations.AddField(
            model_name='reminder',
            name='recipients',
            field=models.ManyToManyField(to='sam2017_app.User', default=None),
        ),
        migrations.AddField(
            model_name='reminder',
            name='reminderType',
            field=models.CharField(default='', max_length=127),
        ),
        migrations.AddField(
            model_name='submission',
            name='reviewers',
            field=models.ManyToManyField(to='sam2017_app.User', blank=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='reviews',
            field=models.ManyToManyField(to='sam2017_app.Review', blank=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 16, 22, 24, 29, 482859)),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(default='Author', max_length=10, choices=[('Author', 'Author'), ('PCM', 'PCM'), ('PCC', 'PCC'), ('Admin', 'Admin')]),
        ),
    ]
