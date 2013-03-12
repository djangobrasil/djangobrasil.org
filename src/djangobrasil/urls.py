#
#  Copyright (c) 2007, 2008 The Django Brasil Community Website Authors
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


from django.conf.urls.defaults import *
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.contrib import admin
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.base import TemplateView
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from djangobrasil.blog.models import Entry
from djangobrasil.blog.feeds import AtomLatestEntriesFeed, RssLatestEntriesFeed
from djangobrasil.aggregator.models import FeedItem
from djangobrasil.aggregator.feeds import RssCommunityAggregatorFeed, AtomCommunityAggregatorFeed

admin.autodiscover()

from moderation.helpers import auto_discover
auto_discover()

sitemaps = {
    'flatpages': FlatPageSitemap,
    'weblog': GenericSitemap({'queryset': Entry.published.all(), 'date_field': 'pub_date'}, changefreq="never")
}

rss_feeds = {
    'weblog': RssLatestEntriesFeed,
    'comunidade': RssCommunityAggregatorFeed,
}

atom_feeds = {
    'weblog': AtomLatestEntriesFeed,
    'comunidade': AtomCommunityAggregatorFeed,
}



aggregator_info_dict = {
    'queryset': FeedItem.objects.select_related().filter(feed__accepted=True),
    'paginate_by': 15,
}


urlpatterns = patterns('',
    # sitemaps
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap',
                       {'sitemaps': sitemaps}),

    # auth
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),

    # feeds
    (r'^feeds/rss/comunidade/$', RssCommunityAggregatorFeed()),
    (r'^feeds/atom/comunidade/$', AtomCommunityAggregatorFeed()),
    (r'^feeds/rss/weblog/$', RssLatestEntriesFeed()),
    (r'^feeds/atom/weblog/$', AtomLatestEntriesFeed()),

    # admin
    (r'^admin/', include(admin.site.urls)),

    # home page
    (r'^$', TemplateView.as_view(template_name='flatfiles/homepage.html')),

    # home page beta
    (r'^beta/$', TemplateView.as_view(template_name='flatfiles/beta.html')),

    # weblog
    (r'^weblog/', include('djangobrasil.blog.urls')),

    # comunidade
    (r'^comunidade/$', ListView.as_view(queryset=FeedItem.objects.select_related().filter(feed__accepted=True), paginate_by=15)),

    #solicitacao-de-feeds
    (r'^participe-dos-feeds/', 'djangobrasil.aggregator.views.participe_dos_feeds'),

    # contato
    (r'^contato/$', include('contact.urls')),

    # casos de sucesso
    (r'^casos-de-sucesso/', include('djangobrasil.success_cases.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        # static files
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),

        (r'^404$', TemplateView.as_view(template_name='404.html')),

        (r'^500$', TemplateView.as_view(template_name='500.html')),
    )
    #urlpatterns += staticfiles_urlpatterns()
