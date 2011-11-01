#
#  Copyright (c) 2005, the Lawrence Journal-World
#  All rights reserved.
#
#  See LICENSE file in src/djangobrasil/apps/aggregator/ directory.
#

from django.db import models

class Feed(models.Model):
    title = models.CharField(max_length=500)
    email = models.EmailField()
    feed_url = models.URLField(max_length=500)#unique
    public_url = models.URLField(max_length=500)
    is_defunct = models.BooleanField()
    accepted = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)

    class Meta:
        db_table = 'aggregator_feeds'

    def __unicode__(self):
        return unicode(self.title)

class FeedItem(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=500)
    link = models.URLField(max_length=500)
    summary = models.TextField(blank=True)
    date_modified = models.DateTimeField()
    guid = models.CharField(max_length=500)#, unique=True, db_index=True)

    class Meta:
        db_table = 'aggregator_feeditems'
        ordering = ("-date_modified",)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.link
