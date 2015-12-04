from sam2017_app.models import Reminder
from sam2017_app.views.notification import NotificationManager
from sam2017.celery import app

__author__ = 'chris'


@app.task
def add(x, y):
    return x + y


@app.task
def send_reminder(reminder_id):

    notification_manager = NotificationManager()
    reminder = notification_manager.get_reminder(reminder_id)
    notification_manager.send_reminder(reminder)
