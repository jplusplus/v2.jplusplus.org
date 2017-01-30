#!/usr/bin/env python
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 11-Apr-2014
# Last mod : 25-Apr-2014
# -----------------------------------------------------------------------------
import os
from django.utils.translation import ugettext_lazy as _

gettext = lambda s: _(s)
# gettext = lambda s: s

BASE_DIR = os.path.dirname(__file__)
# Django settings for jplusplus project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Bonjour', 'bonjour@jplusplus.org'),
)

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '9%4-c*t!%g06@=#l5xqt*+a)m2w&r@-q(5sn)50v!x0!-krf7%'

# List of callables that know how to import templates from various sources.

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'class': 'django.utils.log.NullHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
        },
        'django.request': {
            'handlers': ['null'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'jplusplus.middleware.DomainNamesMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.transaction.TransactionMiddleware'
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    # 'cms.context_processors.media',
    'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static'
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'mptt',
    'menus',
    'south',
    'compressor',
    'redactor',
    'sekizai',
    'taggit',
    'hvad',
    'adminsortable',
    'rest_framework',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion',
    'jplusplus',
)

LANGUAGES = (
    ## Customize this
    ('en',    u'English'),
    ('fr',    u'Français'),
    ('de',    u'Deutsch'),
    ('pt',    u'Português'),
    ('pt-br', u'Português do Brasil'),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'hide_untranslated': False,
        'redirect_on_fallback': True,
        'public': True,
    },
    1: [
        {
            'redirect_on_fallback': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'public': True,
        },
        {
            'redirect_on_fallback': True,
            'code': 'fr',
            'hide_untranslated': False,
            'name': gettext('fr'),
            'public': True,
        },
        {
            'redirect_on_fallback': True,
            'code': 'de',
            'hide_untranslated': False,
            'name': gettext('de'),
            'public': True,
        },
        {
            'redirect_on_fallback': True,
            'code': 'pt',
            'hide_untranslated': False,
            'name': gettext('pt'),
            'public': True,
        },
        {
            'redirect_on_fallback': True,
            'code': 'pt-br',
            'hide_untranslated': False,
            'name': gettext('pt-br'),
            'public': True,
            'fallbacks': ['pt', 'en'],
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('home.html', 'Home'),
    # ('chapter.html', 'Chapter'),
    # ('page.html', 'Page'),
    ('page_with_header.html', 'Page with header'),
    ('page_article.html', 'Article with header'),
    ('chapter.html', 'Chapter'),
    ('chapter_paris_berlin.html', 'Chapter Paris/Berlin'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default':
        {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'development.db', 'HOST': 'localhost', 'USER': '', 'PASSWORD': '', 'PORT': ''}
}

CMS_STYLE_NAMES = (
    # ('header__title', gettext("Header title")),
    ('container', gettext("Container")),
)

COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --bare --compile --stdio'),
    ('text/less', 'lessc --include-path="%s" {infile} {outfile}' % (os.path.join(STATICFILES_DIRS[0], 'less'))),
)

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.UnicodeJSONRenderer',
    )
}

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

COMPRESS_ENABLED           = True
COMPRESS_CSS_FILTERS       = (
    # "compressor.filters.cssmin.CSSMinFilter",
    "compressor.filters.template.TemplateFilter",
    'compressor.filters.css_default.CssAbsoluteFilter',
)
COMPRESS_TEMPLATE_FILTER_CONTEXT = {
    'STATIC_URL': STATIC_URL
}

REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD  = 'uploads/'
UUIDUploader     = 'redactor.handlers.DateDirectoryUploader'

# EMAILS
EMAIL_SUBJECT_PREFIX  = "[J++] "
EMAIL_BACKEND         = 'django.core.mail.backends.console.EmailBackend'

# Sites for DomainNamesMiddleware (in `sources/jplusplus/middleware.py`)
SITES = { # from_url : to_page_reverse_id
    "porto.jplusplus.dev:8000"  : "paris-berlin",
    "berlin.jplusplus.dev:8000" : "paris-berlin",
}

# Thumbnails
THUMBNAILS_PROJECTS      = {'small':(265, 159), 'normal':(945, 640)}
THUMBNAILS_TROMBINOSCOPE = {                    'normal':(200, 200)}

# EOF
