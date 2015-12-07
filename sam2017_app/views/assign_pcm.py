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
from sam2017_app.models import submission
from sam2017_app.models.review import Review, Paper
from sam2017_app.models.submission_choice import SubmissionChoice

def onAssignPCM(request, submission_id):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')
    user = User.objects.get(email=request.session['user_email'])
    all_pcms = User.objects.all().filter(type='PCM')
    paper = submission.Submission.objects.get(id=int(submission_id)).paper
    pcmSets =[]
    for pcm in all_pcms:
        assigned = Review.objects.filter(paper=paper,reviewer=pcm).exists()
        if(assigned == False):
            chosen = SubmissionChoice.objects.filter(chooser=pcm, choice=submission.Submission.objects.filter(id=int(submission_id))).exists()
            pcmSets.append((pcm,chosen))
    context = {
        'pcms_list': pcmSets,
        'paper_id': submission_id,
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

    rev = Review()

    pcm = User.objects.get(id = pcm_id)

    current_submission = submission.Submission.objects.get(id=submission_id)

    paper = getattr(current_submission, 'paper')

    rev.reviewer = pcm
    rev.paper = paper
    rev.save()

    current_submission.reviews.add(rev)
    current_submission.save()

    return HttpResponseRedirect('/user_profile')

