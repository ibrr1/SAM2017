from sam2017_app.models import paper
from sam2017_app.models.user_model import User
from sam2017_app.forms.paper_form import PaperSubmission
from django.shortcuts import render
from django.http import HttpResponseRedirect
from sam2017_app.views.session import __is_session_open
from sam2017_app.views.user_details import __add_general_content_to_context
from django.contrib import messages


def paper_submission(request):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])

    paper_submission_form = PaperSubmission(request.POST or None)

    context = {
        'paper_submission_form': paper_submission_form,
    }

    context.update(__add_general_content_to_context(user))

    if request.method == "POST":
        paper_submission_form = PaperSubmission(request.POST, request.FILES)
        if paper_submission_form.is_valid():
            filename = request.FILES['paper'].name
            if not (filename.endswith('.pdf') or (filename.endswith('.doc')) or (filename.endswith('.docx'))):
                error = 'sorry!! you can only submit a PDF or Word document'
                context['error'] = error
            else:

                submitted_paper = paper.Paper()
                submitted_paper.paper = filename
                submitted_paper.title = paper_submission_form.cleaned_data['title']
                submitted_paper.authors_list = paper_submission_form.cleaned_data['authors_list']
                submitted_paper.author_contact = paper_submission_form.cleaned_data['author_contact']
                submitted_paper.paper_format = paper_submission_form.cleaned_data['paper_format']
                submitted_paper.submitter = user
                submitted_paper.save()

                return HttpResponseRedirect('/user_profile')

    return render(request, 'paper_submission.html', context)

# End paper submission
