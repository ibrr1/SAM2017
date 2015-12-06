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
from sam2017_app.forms.pcc_rate_form import PCC_Rate


def pcc_rating(request):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])

    all_Submission = Submission.objects.all()


    context = {
        'all_submission': all_Submission,
        'rate_paper_page': True,

    }

    context.update(__add_general_content_to_context(user))

    return render(request, 'pcc_rate_paper.html', context)



def view_rating(request, paper_id):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])
    curent_reviews = Review.objects.all().filter(paper = paper_id)
    pcc_form = PCC_Rate(request.POST or None)



    print(paper_id)


    context = {
        'pcc_rate_form': pcc_form,
        'review':curent_reviews
    }

    if pcc_form.is_valid():
        # current_review = review.Review()

        current_submission = Submission.objects.all().get(paper = paper_id)
        current_submission.rating = pcc_form.cleaned_data['rating']

        current_submission.save()

        return HttpResponseRedirect('/user_profile')

    context.update(__add_general_content_to_context(user))

    return render(request, 'pcc_view_reviews.html', context)


