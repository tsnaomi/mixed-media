# settings/production.py

from .base import *  # noqa

SITE_URL = ''  # TODO

DEBUG = False

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'newsfeed/templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
        'debug': DEBUG,
    },
    }]

STATIC_URL = '/static/'  # TODO
