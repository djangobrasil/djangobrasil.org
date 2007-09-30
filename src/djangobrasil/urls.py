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


from django.conf.urls.defaults import *
from django.contrib.comments.feeds import LatestFreeCommentsFeed
from django.contrib.comments.models import FreeComment
from django.contrib import databrowse
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from djangobrasil import settings
from djangobrasil.apps.blog.models import Entry
from djangobrasil.apps.blog.feeds import AtomLatestEntriesFeed, RssLatestEntriesFeed
from djangobrasil.apps.aggregator.models import FeedItem
from djangobrasil.apps.aggregator.feeds import RssCommunityAggregatorFeed, AtomCommunityAggregatorFeed


databrowse.site.register(Entry)
databrowse.site.register(FeedItem)
databrowse.site.register(FreeComment)

comments_info_dict = {
    'queryset': FreeComment.objects.all(),
    'paginate_by': 15,
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'weblog': GenericSitemap({'queryset': Entry.published.all(), 'date_field': 'pub_date'}, changefreq="never")
}

rss_feeds = {
    'weblog': RssLatestEntriesFeed,
    'comments': LatestFreeCommentsFeed,    
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

    # static files
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                              {'document_root': settings.MEDIA_ROOT}),

    # sitemaps
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', 
                       {'sitemaps': sitemaps}),

    # auth
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    (r'^accounts/logout/', 'django.views.auth.login.logout'),

    # feeds
    (r'^feeds/rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': rss_feeds}),
    (r'^feeds/atom/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': atom_feeds}),

    # comments
    (r'^comments/$', 'django.views.generic.list_detail.object_list', comments_info_dict),
    (r'^comments/', include('django.contrib.comments.urls.comments')),

    # databrowse
    (r'^db/(.*)', 'djangobrasil.views.db'),

    # admin
    (r'^admin/', include('django.contrib.admin.urls')),

    # home page
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'flatfiles/homepage.html'}),

    # weblog
    (r'^weblog/', include('djangobrasil.apps.blog.urls')),

    # comunidade
    (r'^comunidade/$', 'django.views.generic.list_detail.object_list', aggregator_info_dict),

    # contato
    (r'^contato/$', 'djangobrasil.views.contact'),
    #(r'^contato/$', 'django.views.generic.simple.direct_to_template', {'template': 'flatfiles/contato.html'}),

)
