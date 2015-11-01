from sam2017_app import models
from django.shortcuts import render
from django.http import HttpResponseRedirect
from sam2017_app.views.session import __is_session_open
from sam2017_app.views.user_details import __add_general_content_to_context


# end __is_session_open

def user_profile(request):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = models.User.objects.get(email=request.session['user_email'])

    context = {
        'user_type' : user.type
    }

    context.update(__add_general_content_to_context(user))

    return render(request, 'user_profile.html', context)

# end profile




