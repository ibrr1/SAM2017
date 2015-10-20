import datetime
from . import forms, models
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages



def user_registration(request):
    form_personal_info = forms.UserRegistrar(request.POST or None)

    context = {
        'form_user_personal_information': form_personal_info,
    }

    if form_personal_info.is_valid():
        user = models.User()

        user.email = form_personal_info.cleaned_data['email']
        user.first_name = form_personal_info.cleaned_data['first_name']
        user.last_name = form_personal_info.cleaned_data['last_name']
        user.password = form_personal_info.cleaned_data['password']

        registered = models.User.objects.filter(email=user.email)

        # check if there is an existent user with the email entered by the user trying to register
        if len(registered) > 0:
            error = 'User already registered.'
            context['error'] = error

        else:
            # store the user in the db
            user.save()

            return __login_open_session(request, user.email)

    return render(request, 'registration.html', context)


# end user_registration

def __login_open_session(request, email):
    # open the session
    request.session['is_open'] = True
    # set the universal user accessor
    request.session['user_email'] = email

    return HttpResponseRedirect('/user_profile')


# end __login_open_session


def user_login(request):
    form = forms.UserLogger(request.POST or None)

    context = {
        'login_form': form,
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


def __is_session_open(request):
    # verify if a session has been open or not
    return request.session['is_open']


# end __is_session_open


def user_profile(request):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = models.User.objects.get(email=request.session['user_email'])

    context = {
    }

    context.update(__add_general_content_to_context(user))

    return render(request, 'user_profile.html', context)

# end profile

# private function dedicated to the addition of common fields in context
def __add_general_content_to_context(user):
    context = {
        'user_first_name': user.first_name,
        'date': datetime.date.today(),
    }

    if user.admin == True:
        context['user_first_name'] += ' ( admin )'

    return context


# end register_new_shed


def logout(request):
    request.session['is_open'] = False  # close the session
    return HttpResponseRedirect('/')


# end logout



# User Manage Account
def manage_account(request):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = models.User.objects.get(email=request.session['user_email'])


    # put all the initial for fields in this dict
    initial_form_data = {'first_name': user.first_name,
                         'last_name': user.last_name,
                         'password': user.password,
                         'password_verification': user.password,
                         }

    if request.method == 'GET':
        form_personal_info = forms.ManageAccount(initial_form_data)

        context = {
            'form_user_personal_information': form_personal_info,
        }

        context.update(__add_general_content_to_context(user))

    if request.method == 'POST':
        form_personal_info = forms.ManageAccount(request.POST or None)

        context = {
            'form_user_personal_information': form_personal_info,
        }

        context.update(__add_general_content_to_context(user))

        if form_personal_info.is_valid():

            user.first_name = form_personal_info.cleaned_data['first_name']
            user.last_name = form_personal_info.cleaned_data['last_name']
            user.password = form_personal_info.cleaned_data['password']

            # store the user in the db
            user.save()
            messages.success(request, 'You have successfully updated your information')
            return HttpResponseRedirect('/user_profile')

    return render(request, 'manage_account.html', context)

    # End manage account
