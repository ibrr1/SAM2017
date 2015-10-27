from django.db import models


# This is a user class
class User(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)

    class Meta:
        app_label = 'sam2017_app'
        abstract = True

    def __str__(self):
        return self.email


class Author(User):

    class Meta:
        app_label = 'sam2017_app'


class PCC(Author):

    class Meta:
        app_label = 'sam2017_app'


class PCM(User):

    class Meta:
        app_label = 'sam2017_app'


class Admin(User):

    class Meta:
        app_label = 'sam2017_app'