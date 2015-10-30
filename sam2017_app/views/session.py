from django.http import HttpResponseRedirect

def __login_open_session(request, email):
    # open the session
    request.session['is_open'] = True
    # set the universal user accessor
    request.session['user_email'] = email

    return HttpResponseRedirect('/user_profile')
# end __login_open_session

def __is_session_open(request):
    # verify if a session has been open or not
    return request.session['is_open']