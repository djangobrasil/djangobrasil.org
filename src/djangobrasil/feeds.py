# -*- coding: utf-8 -*-
#
#  Copyright (c) 2008 The Django Brasil Community Website Authors
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

from django.conf import settings
from django.contrib import comments
from django.contrib.comments.feeds import LatestCommentFeed

class DjangoBrasilCommentFeed(LatestCommentFeed):

    def title(self):
        if not hasattr(self, '_site'):
            self._site = Site.objects.get_current()
        return u"Comentários em %s" % self._site.name

    def description(self):
        if not hasattr(self, '_site'):
            self._site = Site.objects.get_current()
        return u"Últimos comentários em %s" % self._site.name

    def items(self):
        qs = comments.get_model().objects.filter(
            site__pk = settings.SITE_ID,
            is_public = True,
            is_removed = False,
        ).order_by('-submit_date')
        if getattr(settings, 'COMMENTS_BANNED_USERS_GROUP', None):
            where = ['user_id NOT IN (SELECT user_id FROM auth_users_group WHERE group_id = %s)']
            params = [settings.COMMENTS_BANNED_USERS_GROUP]
            qs = qs.extra(where=where, params=params)
        return qs[:40]

