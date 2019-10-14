from .base import *

DEBUG = False
ALLOWED_HOSTS = '127.0.0.1'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}
