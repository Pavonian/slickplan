"""Development settings and globals."""

from .base import *


# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# END DEBUG CONFIGURATION

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'slickplan',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mosaicbloom',
#         'USER': 'root',
#         'PASSWORD': 'sqlmicry',
#         'HOST': '172.31.6.24',
#         'PORT': '',
#     }
# }
# END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## Email configuration
# Route email through Amazon SES via Celery
#EMAIL_BACKEND = 'seacucumber.backend.SESBackend'
#MAILER_EMAIL_BACKEND = 'seacucumber.backend.SESBackend'

DEFAULT_FROM_EMAIL = 'leduanf@gmail.com'
EMAIL_HOST_USER = 'leduanf'
EMAIL_HOST_PASSWORD = 'Columbia.1060.'
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH= 'tmp'
########## END Email configuration

WKHTMLTOPDF_CMD = 'C:\\Program Files\\wkhtmltopdf\\bin\\'