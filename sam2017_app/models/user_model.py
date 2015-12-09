from django.db import models


# This is a user class
class User(models.Model):

    AUTHOR = "Author"
    PCM = "PCM"
    PCC = "PCC"
    ADMIN = "Admin"

    USER_TYPE = ((AUTHOR, "Author"), (PCM, "PCM"), (PCC, "PCC"), (ADMIN, "Admin"))

    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=USER_TYPE, default=AUTHOR)
    admin = models.BooleanField(default=False)

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    @classmethod
    def create(cls, first_name, last_name, email, password):
        user = cls(first_name=first_name, last_name=last_name, email=email,
                   password=password)

        return user

    class Meta:
        app_label = 'sam2017_app'

    def __str__(self):
        return "Name: {0} Email:{1}".format(self.full_name, self.email)
