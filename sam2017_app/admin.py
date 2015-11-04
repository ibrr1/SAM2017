from django.contrib import admin
from sam2017_app.models import User, Paper, review, submission, notification

admin.site.register(User)
admin.site.register(Paper)
admin.site.register(review.Review)
admin.site.register(submission.Submission)
admin.site.register(notification.Notification)



