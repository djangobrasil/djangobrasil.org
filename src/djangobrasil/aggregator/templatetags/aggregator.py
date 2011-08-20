#
#  Copyright (c) 2005, the Lawrence Journal-World
#  All rights reserved.
#
#  See LICENSE file in src/djangobrasil/apps/aggregator/ directory.
#


from django import template
from djangobrasil.aggregator.models import Feed

class FeedListNode(template.Node):
    def __init__(self, varname):
        self.varname = varname

    def render(self, context):
        context[self.varname] = Feed.objects.filter(is_defunct=False).order_by('title')
        return ''

def do_get_feed_list(parser, token):
    """
    {% get_feed_list as feed_list %}
    """
    bits = token.contents.split()
    if len(bits) != 3:
        raise template.TemplateSyntaxError, "'%s' tag takes two arguments" % bits[0]
    if bits[1] != "as":
        raise template.TemplateSyntaxError, "First argument to '%s' tag must be 'as'" % bits[0]
    return FeedListNode(bits[2])

register = template.Library()
register.tag('get_feed_list', do_get_feed_list)
