# -*- coding: utf-8 -*-

from settings import *
import os
import dj_database_url

# Allow all host headers
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default' : dj_database_url.config()
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Turn on database level autocommit
# Otherwise db can raise a "current transaction is aborted,
# commands ignored until end of transaction block"
DATABASES['default']['OPTIONS'] = {'autocommit': True,}


# AWS ACCESS
AWS_ACCESS_KEY_ID          = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY      = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME    = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH       = False
AWS_S3_FILE_OVERWRITE      = os.getenv('AWS_S3_FILE_OVERWRITE') == "True" and True or False

# Enable debug for minfication
DEBUG                      = bool(os.getenv('DEBUG', False))

# Configure static files for S3
STATIC_URL                 = os.getenv('STATIC_URL')
INSTALLED_APPS            += ('storages',)
DEFAULT_FILE_STORAGE       = 'storages.backends.s3boto.S3BotoStorage'
# Static storage
STATICFILES_STORAGE        = DEFAULT_FILE_STORAGE
ADMIN_MEDIA_PREFIX         = STATIC_URL + 'admin/'

# JS/CSS compressor settings
COMPRESS_ENABLED           = True
COMPRESS_ROOT              = STATIC_ROOT
COMPRESS_URL               = STATIC_URL
COMPRESS_STORAGE           = STATICFILES_STORAGE
COMPRESS_OFFLINE           = False

# Activate CSS minifier
# COMPRESS_CSS_FILTERS       = (
#     "compressor.filters.cssmin.CSSMinFilter",
#     "compressor.filters.template.TemplateFilter",
# )

COMPRESS_JS_FILTERS = (
    # "compressor.filters.jsmin.JSMinFilter",
    "compressor.filters.template.TemplateFilter",
)

COMPRESS_TEMPLATE_FILTER_CONTEXT = {
    'STATIC_URL': STATIC_URL
}

# Activate the cache, for true
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache',
    }
}

# EMAILS
INSTALLED_APPS      += ('djrill',)
MANDRILL_API_KEY     = os.getenv('MANDRILL_APIKEY')
SERVER_EMAIL         = os.getenv('MANDRILL_USERNAME')
EMAIL_BACKEND        = "djrill.mail.backends.djrill.DjrillBackend"

# EOF
