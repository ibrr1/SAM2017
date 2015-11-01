from django.db import models
from sam2017_app.models import user_model
import datetime


class Paper(models.Model):

    paper = models.FileField(upload_to='submitted_paper')
    title =  models.CharField(max_length=30, blank=False)
    authors_list = models.CharField(max_length=30, blank=False)
    author_contact = models.CharField(max_length=30, blank=False)
    paper_format = models.CharField(max_length=30, blank=False)
    submitter = models.ForeignKey(user_model.User)
    revision_paper = models.CharField(max_length=30)
    is_new_paper = models.BooleanField(default= False)
    date_created = models.DateTimeField(default = datetime.datetime.now())

    class Meta:
        app_label = 'sam2017_app'

    def __str__(self):
        return self.title


class Review(models.Model):

    class Meta:
        app_label = 'sam2017_app'


class Report(models.Model):

    class Meta:
        app_label = 'sam2017_app'


