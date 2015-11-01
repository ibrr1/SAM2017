from django.db import models


# This is a user class
class User(models.Model):

    AUTHOR = "Author"
    PCM = "PCM"
    PCC = "PCC"
    ADMIN = "admin"

    USER_TYPE = ((AUTHOR, "Author"), (PCM, "PCM"), (PCC, "PCC"), (ADMIN, "Admin"))

    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=USER_TYPE, default=AUTHOR)
    admin = models.BooleanField(default=False)

    class Meta:
        app_label = 'sam2017_app'

    def __str__(self):
        return self.email