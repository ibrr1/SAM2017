from sam2017_app.models.notification import Notification, Reminder


class NotificationManager:

    __slots__ = 'reminders'

    @classmethod
    def create(cls):
        # get reminders from the database that are current
        notification_manager = cls()
        notification_manager.reminders = Reminder.objects.all()
        return notification_manager

    def __save_notification_to_user(self, recipient, notification):
        notification.user = recipient
        notification.save()

    def __create_notification(self, notification_type, message):
        # create a notification and return it
        notification = Notification.create(notification_type, message)
        return notification

    def __send_reminder(self, reminder):
        # access the notification in the reminder
        notification = reminder.notification

        for recipient in reminder.recipients:
            # add the notification to the necessary users
            self.__save_notification_to_user(recipient, notification)

    def add_reminder(self, message, reminder_date, recipients):
        notification = self.__create_notification("Reminder", message)
        notification.save()
        reminder = Reminder()
        reminder.notification = notification
        reminder.reminder_date = reminder_date
        reminder.save()
        for recipient in recipients:
            reminder.recipients.add(recipient)

    def send_notification(self, recipients, notification_type, message):
        # create a notification
        notification = self.__create_notification(notification_type, message)

        # save it to the appropriate user(s)
        for recipient in recipients:
            self.__save_notification_to_user(recipient, notification)
