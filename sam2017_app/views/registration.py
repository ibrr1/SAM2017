from sam2017_app.models import user_model
from sam2017_app.forms import registration_form
from sam2017_app.views.session import __login_open_session
from django.shortcuts import render


def user_registration(request):
    form_personal_info = registration_form.UserRegistrar(request.POST or None)

    context = {
        'form_user_personal_information': form_personal_info,
        'registration_page': True
    }

    if form_personal_info.is_valid():
        user = user_model.User()

        user.email = form_personal_info.cleaned_data['email']
        user.first_name = form_personal_info.cleaned_data['first_name']
        user.last_name = form_personal_info.cleaned_data['last_name']
        user.password = form_personal_info.cleaned_data['password']

        registered = user_model.User.objects.filter(email=user.email)

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
