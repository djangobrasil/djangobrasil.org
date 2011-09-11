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
    'queryset': FeedItem.objects.select_related(),
    'paginate_by': 15,
}


urlpatterns = patterns(
    '',

    # sitemaps
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap',
                       {'sitemaps': sitemaps}),

    # auth
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),

    # feeds
    (r'^feeds/rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': rss_feeds}),
    (r'^feeds/atom/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': atom_feeds}),

    # admin
    (r'^admin/', include(admin.site.urls)),

    # home page
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'flatfiles/homepage.html'}),

    # home page beta
    (r'^beta/$', 'django.views.generic.simple.direct_to_template', {'template': 'flatfiles/beta.html'}),

    # weblog
    (r'^weblog/', include('djangobrasil.blog.urls')),

    # comunidade
    (r'^comunidade/$', 'django.views.generic.list_detail.object_list', aggregator_info_dict),

    # contato
    (r'^contato/$', 'djangobrasil.views.contact'),

    # casos de sucesso
    (r'^casos-de-sucesso/', include('djangobrasil.success_cases.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',

        # static files
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),

        (r'^404/$', 'django.views.generic.simple.direct_to_template',
         {'template': '404.html'}),

        (r'^500/$', 'django.views.generic.simple.direct_to_template',
         {'template': '500.html'}),
    )
