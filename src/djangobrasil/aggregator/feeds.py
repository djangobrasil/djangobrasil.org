# -*- coding: utf-8 -*-
#
#  Copyright (c) 2005, the Lawrence Journal-World
#  All rights reserved.
#
#  See LICENSE file

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from djangobrasil.aggregator.models import FeedItem


class RssCommunityAggregatorFeed(Feed):
    title = u"Feeds da comunidade Django Brasil"
    link = u"http://www.djangobrasil.org/comunidade/"
    description = u"Agregador de feeds da comunidade Django Brasil."

    def items(self):
        return FeedItem.objects.all()[:15]


class AtomCommunityAggregatorFeed(RssCommunityAggregatorFeed):
    feed_type = Atom1Feed
    subtitle = u"Agregador de feeds da comunidade Django Brasil"
