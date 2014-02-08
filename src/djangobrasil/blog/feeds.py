# -*- coding: utf-8 -*-
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

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from djangobrasil.blog.models import Entry


class RssLatestEntriesFeed(Feed):
    title = u"Django Brasil Weblog"
    link = u"/weblog/"
    description = u"Blog da comunidade brasileira do framework Django."
    author_name = u'Comunidade Django Brasil'

    def items(self):
        return Entry.published.order_by('-pub_date')[:15]

    def item_pubdate(self, item):
        return item.pub_date


class AtomLatestEntriesFeed(RssLatestEntriesFeed):
    feed_type = Atom1Feed
    subtitle = u"Blog da comunidade brasileira do framework Django"
