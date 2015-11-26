from django.db import models

from sam2017_app.models.paper import Paper
from sam2017_app.models.user_model import User
from sam2017_app.models.review import Review

__author__ = 'Adi'


class Submission(models.Model):

    paper = models.ForeignKey(Paper)
    rating = models.IntegerField(default=0)

    submitter = models.ForeignKey(User, related_name='submitter')
    reviews = models.ManyToManyField(Review, null=True, blank=True)

    class Meta:
        app_label = 'sam2017_app'

    def __str__(self):
        return self.paper.title

