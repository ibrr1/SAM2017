from django.db import models

class SAM2017User(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)

    class Meta:
        app_label = 'sam2017'

    def __str__(self):
        return self.email