#  PROJECT SETTINGS        -*- Mode: Python; -*-
# ---------------------------------------------------------------------
#
# (!)
#
# DON'T CHANGE THIS FILE, USE settings_local.py. YOU GET A TEMPLATE IN
# settings_local.template (COPY HIM TO settings_local.py AND MAKE 
# YOUR NECESSARY CHANGES.
#
# ---------------------------------------------------------------------
#
#  Copyright (c) 2007 Guilherme Mesquita Gondim
#
#  This file is part of Django Brasil Project Site.
#
#  Django Brasil Project is free software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3 of
#  the License, or (at your option) any later version.
#
#  Django Brasil Project is distributed in the hope that it will be
#  useful, but WITHOUT ANY WARRANTY; without even the implied warranty
#  of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import os
BASEDIR = os.path.abspath(os.path.dirname(__file__) + '../../..')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# I can't determine this, use settings_local.py.
ADMINS = ()
MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = BASEDIR + '/db/devel.db'

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

# Used to provide a seed in secret-key hashing algorithms. Set this to
# a random string in your settings_local.py - the longer, the better.
SECRET_KEY = 'set-this-in-your-settings_local.py!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.CacheMiddleware',        
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'djangobrasil.urls'

TEMPLATE_DIRS = (
    BASEDIR + '/templates',
)

FIXTURE_DIRS = (
    BASEDIR + '/src/djangobrasil/fixtures',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.databrowse',
    'django.contrib.redirects',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.comments',    
    'django.contrib.flatpages',
    'djangobrasil.apps.blog',
    'djangobrasil.apps.aggregator',
)


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

