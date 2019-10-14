"""
TODO fare un'app_users e gestire il serializer qua

from movies.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    user_fields = ('id', 'first_name', 'last_name', 'username')
    user_data = UserSerializer(user, context={'request': request}).data
    filtered_user_data = {key: value for key, value in user_data.items() if key in user_fields}
    return {
        'token': token,
        'user': filtered_user_data
    }
"""


# todo qua sotto è temporaneo
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': 'this_user_is_temporary'
    }
