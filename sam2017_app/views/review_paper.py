__author__ = 'Adi'


from sam2017_app.models import user_model
from sam2017_app.models import review
from sam2017_app.forms.review_paper_form import ReviewPaper
from sam2017_app.views.session import __login_open_session
from django.shortcuts import render
from django.http import HttpResponseRedirect
from sam2017_app.views.session import __is_session_open
from sam2017_app import models
from sam2017_app.views.user_details import __add_general_content_to_context


import datetime


def review_paper(request, review_id):

    if not __is_session_open(request):
        return HttpResponseRedirect('/')
    user = models.User.objects.get(email=request.session['user_email'])


    review_paper_form = ReviewPaper(request.POST or None)

    context = {
        'review_paper_form': review_paper_form,
        'review_paper_page': True
    }
    context.update(__add_general_content_to_context(user))


    if review_paper_form.is_valid():
        # current_review = review.Review()

        current_review = review.Review.objects.get(id=review_id)

        current_review.description = review_paper_form.cleaned_data['description']
        current_review.rating = review_paper_form.cleaned_data['rating']
        current_review.date = datetime.datetime.now()
        current_review.is_complete = True

        current_review.save()

        return HttpResponseRedirect('/user_profile')

    return render(request, 'review_paper.html', context)

# end user_registration
