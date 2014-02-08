from django.conf.urls import patterns, url

from contact.views import ContactView


urlpatterns = patterns(
    '',
    url('^$', ContactView.as_view(), name='contact')
)
