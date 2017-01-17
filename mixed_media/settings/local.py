# settings/local.py

from .base import *  # noqa

SITE_URL = '127.0.0.1:8000'


# Debugging -------------------------------------------------------------------

DEBUG = True
TEMPLATE_DEBUG = True

# Static ----------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
