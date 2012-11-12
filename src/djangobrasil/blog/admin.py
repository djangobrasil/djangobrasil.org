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

from django.contrib.admin.options import ModelAdmin
from django.contrib import admin

from models import Entry, ENTRY_DEFAULT_FIELDSET, ENTRY_OTHER_FIELDSET


class EntryAdmin(ModelAdmin):
    list_display = ('title', 'pub_date', 'is_draft')
    list_filter = ('is_draft', 'markup')
    search_fields = ['title', 'slug', 'body']
    date_hierarchy = 'pub_date'
    fieldsets = (
        (None, ENTRY_DEFAULT_FIELDSET),
        ('Other options', ENTRY_OTHER_FIELDSET),
    )
    prepopulated_fields = {
        'slug': ('title',),
    }


admin.site.register(Entry, EntryAdmin)
