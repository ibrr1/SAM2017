import datetime

# private function dedicated to the addition of common fields in context
# private function dedicated to the addition of common fields in context
def __add_general_content_to_context(user):
    context = {
        'user_first_name': user.first_name,
        'user_type': user.type,
        'date': datetime.datetime.now(),
    }

    return context