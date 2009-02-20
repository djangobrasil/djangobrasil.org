#
#  Copyright (c) 2005, the Lawrence Journal-World
#  All rights reserved.
#
#  See LICENSE file in src/djangobrasil/apps/aggregator/ directory.
#

from django.db import models
from urllib2 import HTTPError
from django.conf import settings

class Feed(models.Model):
    title = models.CharField(max_length=500)
    feed_url = models.URLField(unique=True, max_length=500)
    public_url = models.URLField(max_length=500)
    is_defunct = models.BooleanField()

    class Meta:
        db_table = 'aggregator_feeds'

    def __unicode__(self):
        return self.title

class FeedItem(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=500)
    link = models.URLField(max_length=500)
    summary = models.TextField(blank=True)
    date_modified = models.DateTimeField()
    guid = models.CharField(max_length=500, unique=True, db_index=True)

    class Meta:
        db_table = 'aggregator_feeditems'
        ordering = ("-date_modified",)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.link

    @staticmethod
    def post_on_twitter(sender, instance, *args, **kwargs):
        """
        Post every new FeedItem on Twitter.
        """

        # avoid to post the same item twice
        if not kwargs.get('created'):
            return False
        elif not hasattr(settings, 'TWITTER_USERNAME'):
            return False

        # post the new FeedItem on twitter...
        try:
            from twitter import Api

            username = settings.TWITTER_USERNAME
            password = settings.TWITTER_PASSWORD

            # try to post the message on twitter
            message = instance.title.decode('utf-8')
            if len(message) < settings.TWITTER_MAXLENGTH:
               return Api(username, password).PostUpdate(message)

            # ... ok, i quit! your post is too big to twitter
            return False

        # ... but it's ok if it doesn't work because it isn't the main
        # feature of this application :)
        except HTTPError, ex:
            print str(ex)
            return False

models.signals.post_save.connect(FeedItem.post_on_twitter, sender=FeedItem)
