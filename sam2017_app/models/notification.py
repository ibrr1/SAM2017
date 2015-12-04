from django.db import models
from sam2017_app.models.user_model import User


class Notification(models.Model):

    class Meta:
        app_label = 'sam2017_app'

    notification_type = models.CharField(max_length=127, default="")
    message = models.TextField(default="")
    viewed = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="notifications", default=None, null=True)

    @classmethod
    def create(cls, notification_type, message):
        return cls(notification_type=notification_type, message=message)


class Reminder(models.Model):

    class Meta:
        app_label = 'sam2017_app'

    reminder_type = models.CharField(max_length=127, default="")
    reminder_date = models.DateTimeField(default=None)
    recipients = models.ManyToManyField(User, default=None)
    notification = models.OneToOneField(Notification, default=None)

    @classmethod
    def create(cls, reminder_type, reminder_date, recipients, notification):
        return cls(reminder_type, reminder_date, recipients, notification)
