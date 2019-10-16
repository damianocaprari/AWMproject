from app_profiles.serializers import UserSerializerForJWT


def jwt_response_payload_handler(token, user=None, request=None):
    user_data = UserSerializerForJWT(user, context={'request': request}).data
    return {
        'token': token,
        'user': user_data,
    }
