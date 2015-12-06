from sam2017_app.models import paper
from sam2017_app.models.user_model import User
from sam2017_app.forms.paper_form import PaperSubmission
from django.shortcuts import render
from django.http import HttpResponseRedirect
from sam2017_app.views.session import __is_session_open
from sam2017_app.views.user_details import __add_general_content_to_context
from django.contrib import messages
from django.http import HttpResponse
from sam2017_app.models.submission import Submission
from sam2017_app.models.submission_choice import SubmissionChoice

def paper_list(request):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])
    submissionPairs = []
    if user.type == 'Author':
        submissions = Submission.objects.all().filter(submitter_id__exact=user.id)
    else:
        submissions = Submission.objects.all()

        for sub in submissions:
            submissionPairs.append((sub,SubmissionChoice.objects.all().filter(chooser=user,choice=sub).exists()))
    context = {
        'papers_queryset': submissions,
        'user_type': user.type,
        'paper_list_page': True,
        'pairs': submissionPairs,
    }

    context.update(__add_general_content_to_context(user))

    return render(request, 'paper_list.html', context)

def download(request, file_name):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    file = open('submitted_papers/{}'.format(file_name), 'rb')
    response = HttpResponse(file, content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename={}".format(file_name)
    return response

def chooseSubmission(request,submission_id):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])
    if user.type != "PCM":
        return HttpResponseRedirect('/')
    else:
        choice = SubmissionChoice()
        choice.chooser = user
        submission = Submission.objects.get(id= submission_id)
        choice.choice = submission
        choice.save()
        return HttpResponseRedirect('/user_profile/paper_list/')
