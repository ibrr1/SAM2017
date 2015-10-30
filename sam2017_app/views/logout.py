from django.http import HttpResponseRedirect

def logout(request):
    request.session['is_open'] = False  # close the session
    return HttpResponseRedirect('/')