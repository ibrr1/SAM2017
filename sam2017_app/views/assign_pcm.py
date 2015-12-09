from django.shortcuts import render
from django.http import HttpResponseRedirect

from sam2017_app.models.user_model import User
from sam2017_app.views.notification import NotificationManager
from sam2017_app.views.session import __is_session_open
from sam2017_app.views.user_details import __add_general_content_to_context
from sam2017_app.models import submission
from sam2017_app.models.review import Review
from sam2017_app.models.submission_choice import SubmissionChoice

__author__ = 'ibrahim'


def on_assign_pcm(request, submission_id):

    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])
    all_pcms = User.objects.all().filter(type='PCM')
    paper = submission.Submission.objects.get(id=int(submission_id)).paper
    pcm_sets = []

    for pcm in all_pcms:
        assigned = Review.objects.filter(paper=paper, reviewer=pcm).exists()
        if not assigned:
            chosen = SubmissionChoice.objects.filter(chooser=pcm, choice=submission.Submission.objects.filter(id=int(submission_id))).exists()
            pcm_sets.append((pcm, chosen))

    context = {
        'pcms_list': pcm_sets,
        'paper_id': submission_id,
    }

    context.update(__add_general_content_to_context(user))

    return render(request, 'assign_pcm_table.html', context)


def assign_paper(request, submission_id, pcm_id):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])

    context = {}
    context.update(__add_general_content_to_context(user))

    rev = Review()

    pcm = User.objects.get(id=pcm_id)

    current_submission = submission.Submission.objects.get(id=submission_id)

    paper = current_submission.paper

    rev.reviewer = pcm
    rev.paper = paper
    rev.save()

    current_submission.reviews.add(rev)
    current_submission.save()

    try:
        nm = NotificationManager.create()
        nm.send_notification(recipients=[pcm], message="You have been assigned the paper {0} for review".format(paper.title))
    except:
        print("Something went wrong with adding a notification about paper assignment")

    return HttpResponseRedirect('../')

