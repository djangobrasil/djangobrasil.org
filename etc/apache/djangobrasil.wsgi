#!/usr/bin/env python
# -*- mode: python -*-
#
# File path: /srv/webapps/www.djangobrasil.org/online-branch/etc/apache/djangobrasil.wsgi
#

import os, sys

sys.path.insert(0, '/srv/webapps/www.djangobrasil.org/online-branch/src')
sys.path.insert(0, '/srv/webapps/www.djangobrasil.org/online-branch/src/djangobrasil')

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangobrasil.settings'
os.environ['PYTHON_EGG_CACHE'] = '/srv/webapps/www.djangobrasil.org/.python-eggs'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
