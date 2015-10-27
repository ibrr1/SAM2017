__author__ = 'chris'

from sam2017_app.models.user import User, Author, PCC, PCM, Admin

#   Easily Breaks up the models into a models package. If you are to add a model, make sure
#   You do the following:
#   Create the model, and define the Meta Class(within the new class) with app_label = 'sam2017'
#
#   Ex. class User:
#           -- SOME ATTRIBUTES --
#
#           class Meta:
#               app_label = 'sam2017'
#
#   In this file import the file (make certain you order the imports correctly. If Tool has User as a ForeignKey,
#   Make sure User is imported first.
#   Add the name of the class in the __all__ variable

__al__ = ['User', 'Author', 'PCC', 'PCM', 'Admin']