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

def pcms_chosen_paper(request):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])
    pcms_chosen_paper = SubmissionChoice.objects.all()
    print(pcms_chosen_paper)

    context = {
        'ChosenPaper': pcms_chosen_paper,
        'pcm_chosen_paper_page': True,

    }

    context.update(__add_general_content_to_context(user))

    return render(request, 'pcms_chosen_paper_list.html', context)

