from django.db import models
from sam2017_app.models.paper import Paper
from sam2017_app.models.user_model import User

__author__ = 'Adi'


class Review(models.Model):
    paper = models.ForeignKey(Paper, null=True)

    reviewer = models.ForeignKey(User, null=True)

    description = models.CharField(max_length=100, blank=True)

    rating = models.IntegerField(default=0)

    is_complete = models.BooleanField(default=False)

    class Meta:
        app_label = 'sam2017_app'