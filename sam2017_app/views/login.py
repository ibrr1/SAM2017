from django.http import HttpResponseRedirect
from sam2017_app import models
from sam2017_app.forms import login_form
from sam2017_app.views.session import __login_open_session
from django.shortcuts import render

def user_login(request):
    form = login_form.UserLogger(request.POST or None)

    context = {
        'login_form': form,
        'login_page': True,

    }

    if form.is_valid():
        # verify if user with the entered email and password exists
        user = models.User.objects.filter(email=form.cleaned_data['email'], password=form.cleaned_data['password'])


        if not user:
            # if not, store the error message in the context
            error = 'Invalid email or password. Please try again.'
            context['error'] = error

        else:
            return __login_open_session(request, form.cleaned_data['email'])

    return render(request, 'home.html', context)


# end user_login


# end __is_session_open