from django.db import models


class Paper(models.Model):

    class Meta:
        app_label = 'sam2017_app'


class Review(models.Model):

    class Meta:
        app_label = 'sam2017_app'


class Report(models.Model):

    class Meta:
        app_label = 'sam2017_app'