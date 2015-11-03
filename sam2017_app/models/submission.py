from django.db import models

from sam2017_app.models.paper import Paper
from sam2017_app.models.user_model import User
from sam2017_app.models.review import Review

__author__ = 'Adi'


class Submission(models.Model):

    paper = models.ForeignKey(Paper)
    rating = models.IntegerField(default=0)

    submitter = models.ForeignKey(User, related_name='submitter')

    reviewer1 = models.ForeignKey(User, related_name='reviewer1')
    reviewer2 = models.ForeignKey(User, related_name='reviewer2')
    reviewer3 = models.ForeignKey(User, related_name='reviewer3')

    review1 = models.ForeignKey(Review, related_name='review1')
    review2 = models.ForeignKey(Review, related_name='review2')
    review3 = models.ForeignKey(Review, related_name='review3')

    class Meta:
        app_label = 'sam2017_app'