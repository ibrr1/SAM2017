__author__ = 'ibrahim'

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
from sam2017_app.models.review import Review
from sam2017_app.models.submission_choice import SubmissionChoice

def onAssignPCM(request, submission_id):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')
    user = User.objects.get(email=request.session['user_email'])
    subm = Submission.objects.get(id=int(submission_id))
    all_pcms = User.objects.all().filter(type=User.PCM)
    pcmpairs = []
    for pcm in all_pcms:
        pcmpairs.append((pcm,SubmissionChoice.objects.filter(chooser=pcm,choice=subm).exists(),Review.objects.filter(id=int(submission_id),reviewer=pcm).exists()))
    context = {
        'pcms_list': all_pcms,
        'submission_id': submission_id,
        'pcm_pairs': pcmpairs,
    }
    context.update(__add_general_content_to_context(user))

    return render(request, 'assign_pcm_table.html', context)


def AssignPaper(request,submission_id,pcm_id):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])

    context = {
    }
    context.update(__add_general_content_to_context(user))



    context.update(__add_general_content_to_context(user))
    messages.success(request, 'You have successfully updated your information')
    subm = Submission.Submission.objects.get(id = submission_id)
    use = User.objects.get(id = pcm_id)
    rev = Review.Review()
    rev.paper=subm[0]
    rev.reviewer = use[0]

    rev.save()
    return HttpResponseRedirect('/user_profile')

