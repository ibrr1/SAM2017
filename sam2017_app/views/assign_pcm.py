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


def onAssignPCM(request, submission_id):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')
    user = User.objects.get(email=request.session['user_email'])

    all_pcms = User.objects.all().filter(type=User.PCM)

    context = {
        'pcms_list': all_pcms,
    }
    context.update(__add_general_content_to_context(user))

    return render(request, 'assign_pcm_table.html', context)


def AssignPaper(request):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(email=request.session['user_email'])

    context = {
    }
    context.update(__add_general_content_to_context(user))



    context.update(__add_general_content_to_context(user))
    messages.success(request, 'You have successfully updated your information')
    return HttpResponseRedirect('/user_profile')


    return render(request, 'assign_pcm_table.html', context)
