from AWMproject.settings.base import *

DEBUG = False

ALLOWED_HOSTS = '127.0.0.1'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    #'DEFAULT_PARSERS_CLASSES' : [
#        'rest_framework.parsers.JSONParser',
#        'rest_framework.parsers.FileUploadParser',
#        'rest_framework.parsers.MultiPartParser',
#        'rest_framework.parsers.FormParser',
#    ]
}
