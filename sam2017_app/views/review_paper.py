__author__ = 'Adi'


from sam2017_app.models import user_model
from sam2017_app.models import review
from sam2017_app.forms.review_paper_form import ReviewPaper
from sam2017_app.views.session import __login_open_session
from django.shortcuts import render
from django.http import HttpResponseRedirect
from sam2017_app.views.session import __is_session_open
import datetime


def review_paper(request, review_id):

    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    review_paper_form = ReviewPaper(request.POST or None)

    context = {
        'review_paper_form': review_paper_form,
        'review_paper_page': True
    }

    if review_paper_form.is_valid():

        user = user_model.User()

        current_review = review.Review()

        # current_review = review.Review.objects.filter(id=review_id)

        current_review.description = review_paper_form.cleaned_data['description']
        current_review.rating = review_paper_form.cleaned_data['rating']
        current_review.date = datetime.datetime.now()

        current_review.save()

        return __login_open_session(request, user.email)

    return render(request, 'review_paper.html', context)

# end user_registration
