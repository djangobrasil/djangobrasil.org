from unittest import TestCase
from django.template import Template, Context
from djangobrasil.aggregator.models import Feed

class FeedListTagTest(TestCase):

    def setUp(self):
        Feed.objects.create(
            title='Igor',
            feed_url='http://www.igorsobreira.com/feeds/categoria/django/',
            public_url='http://www.igorsobreira.com/',
            is_defunct=False,
        )
        Feed.objects.create(
            title='Enrico',
            feed_url='http://ricobl.wordpress.com/category/django/feed/',
            public_url='http://ricobl.wordpress.com/',
            is_defunct=False,
        )
        Feed.objects.create(
            title='Andrews',
            feed_url='http://www.andrewsmedina.com/rss/',
            public_url='http://www.andrewsmedina.com/',
            is_defunct=False,
        )

    def test_feed_list_should_be_in_alphabetical_order(self):
        html  = u"{% load aggregator %}"
        html += u"{% get_feed_list as feed_list %}"
        html += u"{% for feed in feed_list %}{{ feed }},{% endfor %}"

        result = Template(html).render(Context({}))

        self.assertEquals(u"Andrews,Enrico,Igor,", result)

