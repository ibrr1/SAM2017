from django.db import models
from sam2017_app.models.paper import Paper
from sam2017_app.models.user_model import User
from sam2017_app.models import user_model
from sam2017_app.models.submission import Submission


#A model representing the
class SubmissionChoice(models.Model):
    chooser = models.ForeignKey(User)
    choice = models.ForeignKey(Submission)
    
    class Meta:
        app_label = 'sam2017'
