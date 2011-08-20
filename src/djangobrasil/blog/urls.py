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
from djangobrasil.blog.models import Entry


info_dict = {
    'queryset': Entry.published,
    'date_field': 'pub_date',
}


urlpatterns = patterns(
    'django.views.generic.date_based',
    (r'^(?P<year>\d{4})/(?P<month>[0-9]{2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(info_dict, slug_field='slug', month_format='%m')),
    (r'^(?P<year>\d{4})/(?P<month>[0-9]{2})/(?P<day>\d{1,2})/$', 'archive_day', dict(info_dict, month_format='%m')),
    (r'^(?P<year>\d{4})/(?P<month>[0-9]{2})/$', 'archive_month', dict(info_dict, month_format='%m')),
    (r'^(?P<year>\d{4})/$', 'archive_year', info_dict),
    (r'^/?$', 'archive_index', dict(info_dict, num_latest=5)),
)
