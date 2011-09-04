import os
import sys
import subprocess

from django.conf import settings
from django.test.simple import DjangoTestSuiteRunner

curdir = os.path.abspath(os.path.dirname(__file__))

class DjangoBrasilTestRunner(DjangoTestSuiteRunner):

    def __init__(self, verbosity=2, **kwargs):
        self.verbosity = verbosity
        self.interactive = True
        settings.DEBUG = False

    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        args = ['nosetests', '--verbosity=2']

        app_names = [app for app in settings.INSTALLED_APPS
                     if app.split('.')[0] != 'django' and app != 'lettuce.django' and app not in settings.SKIP_TESTS]

        if sys.argv[-1] in ('unit', 'functional', 'acceptance'):
            kind = sys.argv[-1]
            apps = ["%s/tests/%s" % (app_name, kind) for app_name in app_names if os.path.isdir("%s/tests/%s" % (app_name, kind))]
        else:
            apps = app_names

        args.extend(apps)

        old_config = self.setup_databases()
        result = subprocess.call(args)
        self.teardown_databases(old_config)

        return result
