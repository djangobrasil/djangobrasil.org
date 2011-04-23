from django.conf.urls.defaults import *

urlpatterns = patterns('apps.success_cases.views',
    (r'^$', 'all_cases'),
    (r'novo/$', 'new_case'),
#    (r'^post/(?P<slug>[\w_-]+)/$', 'post'),
)
