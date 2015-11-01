from sam2017_app import models
from django.shortcuts import render
from django.http import HttpResponseRedirect
from sam2017_app.views.session import __is_session_open
from sam2017_app.views.user_details import __add_general_content_to_context
from sam2017_app.models import paper
from django.contrib import messages

def user_profile(request):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = models.User.objects.get(email=request.session['user_email'])

    # get all papers
    papers = paper.Paper.objects.all();

    if user.type == 'PCC':
        for submitted_paper in papers:
            if submitted_paper.is_new_paper == True:
                submitter_first_name = submitted_paper.submitter.first_name
                submitter_last_name = submitted_paper.submitter.last_name
                date = submitted_paper.date_created.strftime("%m/%d/%Y %H:%M")
                messages.info(request,'New paper has been submitted by: ' + submitter_first_name + ' ' + submitter_last_name + ' at: ' + str(date))
                submitted_paper.is_new_paper = False
                submitted_paper.save()

    context = {
        'user_type': user.type,
    }

    context.update(__add_general_content_to_context(user))

    return render(request, 'user_profile.html', context)

# end profile
