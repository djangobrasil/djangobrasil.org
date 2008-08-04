#
#  Copyright (c) 2005, the Lawrence Journal-World
#  All rights reserved.
#
#  See LICENSE file in src/djangobrasil/apps/aggregator/ directory.
#

from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from djangobrasil.apps.aggregator.models import Feed

class FeedAdmin(ModelAdmin):
    list_display = ("title", "public_url", "is_defunct")
    list_filter = ("is_defunct",)
    ordering = ("title",)
    search_fields = ("title", "public_url")
    list_per_page = 500

admin.site.register(Feed, FeedAdmin)
