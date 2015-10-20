from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email
