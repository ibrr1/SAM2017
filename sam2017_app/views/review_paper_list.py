__author__ = 'Adi'


from sam2017_app.models import review
from sam2017_app.models.user_model import User
from sam2017_app.forms.paper_form import PaperSubmission
from django.shortcuts import render
from django.http import HttpResponseRedirect
from sam2017_app.views.session import __is_session_open
from sam2017_app.views.user_details import __add_general_content_to_context
from django.contrib import messages
from django.http import HttpResponse
from sam2017_app.models import submission


def review_paper_list(request):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])

    reviews = review.Review.objects.filter(reviewer=user.id)

    # papers = submission.Submission.objects.all()

    print(user.id)
    print(reviews)

    context = {
        'papers_queryset': reviews,
        'user_type': user.type,
        'review_paper_list_page': True
    }

    context.update(__add_general_content_to_context(user))

    return render(request, 'review_paper_list.html', context)


def download(request, file_name):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    file = open('submitted_papers/{}'.format(file_name), 'rb')
    response = HttpResponse(file, content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename={}".format(file_name)
    return response

