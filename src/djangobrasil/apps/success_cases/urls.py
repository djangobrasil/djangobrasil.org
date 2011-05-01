from django.conf.urls.defaults import *

urlpatterns = patterns('apps.success_cases.views',
    (r'^$', 'all_cases'),
    (r'^novo/$', 'new_case'),
    (r'^(?P<slug>[\w_-]+)/$', 'specific_case'),
)
