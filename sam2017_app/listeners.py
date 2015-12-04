from django.db.models.signals import post_save
from sam2017_app.models.notification import Reminder
from sam2017_app.tasks import send_reminder

__author__ = 'chris'


def reminder_handler(*args, **kwargs):
    reminder = kwargs.get('instance')
    send_reminder.apply_async(eta=reminder.reminder_date, kwargs={'reminder_id': reminder.id})

post_save.connect(reminder_handler, sender=Reminder)
