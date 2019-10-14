from .base import *

ALLOWED_HOSTS = ['192.168.1.85', 'localhost', '127.0.0.1']

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    ],
}
