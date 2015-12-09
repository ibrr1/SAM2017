from django.shortcuts import render
from django.http import HttpResponseRedirect

from sam2017_app.models.user_model import User
from sam2017_app.views.notification import NotificationManager
from sam2017_app.views.session import __is_session_open
from sam2017_app.views.user_details import __add_general_content_to_context
from sam2017_app.models.submission import Submission
from sam2017_app.models.review import Review
from sam2017_app.forms.pcc_rate_form import PCC_Rate

__author__ = 'ibrahim'


def pcc_rating(request):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])

    all_submission = Submission.objects.all()

    context = {
        'all_submission': all_submission,
        'rate_paper_page': True,

    }

    context.update(__add_general_content_to_context(user))

    return render(request, 'pcc_rate_paper.html', context)


def view_rating(request, paper_id):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])
    curent_reviews = Review.objects.all().filter(paper=paper_id)
    pcc_form = PCC_Rate(request.POST or None)

    context = {
        'pcc_rate_form': pcc_form,
        'rate_paper_page': True,
        'review': curent_reviews
    }

    if pcc_form.is_valid():

        current_submission = Submission.objects.all().get(paper=paper_id)
        current_submission.rating = pcc_form.cleaned_data['rating']

        current_submission.save()

        try:
            nm = NotificationManager.create()
            nm.send_notification(recipients=[current_submission.submitter], message="Your submission for the paper \"{0}\", has been given the rating: {1}".format(current_submission.paper.title, current_submission.rating))
        except:
            print("There was a problem sending the notification for a rated paper")

        return HttpResponseRedirect('/user_profile')

    context.update(__add_general_content_to_context(user))

    return render(request, 'pcc_view_reviews.html', context)


