import datetime

# private function dedicated to the addition of common fields in context
# private function dedicated to the addition of common fields in context
def __add_general_content_to_context(user):
    context = {
        'user_first_name': user.first_name,
        'date': datetime.date.today(),
    }

    if user.admin == True:
        context['user_first_name'] += ' ( admin )'

    return context