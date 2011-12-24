import os


BASEDIR = os.path.abspath(os.path.dirname(__file__) + '../../..')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# I can't determine this, use settings_local.py.
ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASEDIR, 'etc/devel.db')
    }
}

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'
SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = BASEDIR + '/media/'
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin_media/'

CACHE_BACKEND = 'dummy:///'
CACHE_MIDDLEWARE_SECONDS = 60 * 5       # 5 minutes
CACHE_MIDDLEWARE_KEY_PREFIX = 'djangobrasil'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

SECRET_KEY = 'set-this-in-your-settings_local.py!'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'djangobrasil.urls'

TEMPLATE_DIRS = (
    BASEDIR + '/src/djangobrasil/templates',
)

FIXTURE_DIRS = (
    BASEDIR + '/src/djangobrasil/fixtures',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'django.contrib.markup',

    'blog',
    'aggregator',
    'success_cases',
    'recaptcha_works',
    'moderation',
    'contact',
    'django_nose',
)

RECAPTCHA_PUBLIC_KEY  = '6LfYNcQSAAAAAD1zXvNHZyJ-VlJPLv1j56n54rZE'
RECAPTCHA_PRIVATE_KEY = 'chave privada do recaptcha'
RECAPTCHA_USE_SSL = True
RECAPTCHA_OPTIONS = {
    'theme': 'red',
    'lang': 'pt',
    'tabindex': 0,
}

try:
    from settings_local import *
except ImportError:
    from warnings import warn
    msg = "You don't have settings_local.py file, using defaults settings."
    try:
        # don't work in Python 2.4 or before
        warn(msg, category=ImportWarning)
    except NameError:
        warn(msg)
