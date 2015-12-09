from django.db import models
from sam2017_app.models.paper import Paper

import datetime

from sam2017_app.models.user_model import User

__author__ = 'Adi'


class Review(models.Model):
    paper = models.ForeignKey(Paper, null=True)
    reviewer = models.ForeignKey(User, null=True, blank=True)
    description = models.CharField(max_length=100, blank=True)
    rating = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.datetime.now())
    is_complete = models.BooleanField(default=False)

    class Meta:
        app_label = 'sam2017_app'


class ReviewDeadline(models.Model):
    review_deadline = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        app_label = 'sam2017_app'

    def __str__(self):
        return "review dead line"