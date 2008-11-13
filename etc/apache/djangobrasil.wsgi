#!/usr/bin/env python
# -*- mode: python -*-
#
# File path: /srv/webapps/www.djangobrasil.org/etc/apache/djangobrasil.wsgi
#

import os, sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '../..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangobrasil.settings'
os.environ['PYTHON_EGG_CACHE'] = '/srv/webapps/www.djangobrasil.org/.python-eggs'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
