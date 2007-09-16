#
#  Copyright (c) 2007 Guilherme Mesquita Gondim
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


from django import template
from djangobrasil.apps.blog.models import Entry


class BlogEntriesNode(template.Node):
    def __init__(self, start, stop, varname):
        self.start, self.stop, self.varname = int(start), int(stop), varname

    def render(self, context):
        context[self.varname] = list(Entry.published.all()[self.start-1:self.stop])
        return ''

def do_get_blog_entries(parser, token):
    """
    {% get_blog_entries 1 to 10 as latest_entries %}
    {% get_blog_entries 11 to 20 as old_entries %}
    """
    bits = token.contents.split()
    if len(bits) != 6:
        raise template.TemplateSyntaxError, "'%s' tag takes six arguments" % bits[0]
    if bits[2] != 'to':
        raise template.TemplateSyntaxError, "Second argument to '%s' tag must be 'to'" % bits[0]
    if bits[4] != 'as':
        raise template.TemplateSyntaxError, "Fourth argument to '%s' tag must be 'as'" % bits[0]
    return BlogEntriesNode(bits[1], bits[3], bits[5])


class MonthListNode(template.Node):
    def __init__(self, varname):
        self.varname = varname

    def render(self, context):
        context[self.varname] = list(Entry.published.dates("pub_date", "month", order="DESC"))
        return ''

def do_get_blog_month_list(parser, token):
    """
    {% get_blog_month_list as archive %}
    {% get_blog_month_list as blog_months %}
    """
    bits = token.contents.split()
    if len(bits) != 3:
        raise template.TemplateSyntaxError, "'%s' tag takes three arguments" % bits[0]
    if bits[1] != 'as':
        raise template.TemplateSyntaxError, "First argument to '%s' tag must be 'as'" % bits[0]
    return MonthListNode(bits[2])


register = template.Library()
register.tag('get_blog_entries', do_get_blog_entries)
register.tag('get_blog_month_list', do_get_blog_month_list)
