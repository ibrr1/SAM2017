from django.contrib import admin
from sam2017_app.models import User, paper

admin.site.register(User)
admin.site.register(paper.Paper)

