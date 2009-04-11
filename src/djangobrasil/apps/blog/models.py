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


from datetime import datetime
from django.db import models
from djangobrasil.signals import post_to_twitter

MARKUP_CHOICES = (
    ('markdown', 'Markdown'),
    ('rest',     'reStructuredText'),
    ('textile',  'Textile'),
    ('raw',      'Raw HTML'),
)

ENTRY_DEFAULT_FIELDSET = {
    'fields': ('title', 'slug', 'body_source', 'is_draft',),
}
ENTRY_OTHER_FIELDSET = {
    'fields': ('markup', 'pub_date',),
    'classes': 'collapse',
}


def markuping(markup, value):
    """
    Transform plain text markup syntaxes to HTML with filters in 
    django.contrib.markup.templatetags.
    """
    from django.contrib.markup.templatetags.markup \
        import textile, markdown, restructuredtext
    if markup == 'markdown':
        return markdown(value)
    elif markup == 'rest':
        return restructuredtext(value)
    elif markup == 'textile':
        return textile(value)
    else:
        return value            # raw


class PublishedEntriesManager(models.Manager):
    def get_query_set(self):
        queryset = super(PublishedEntriesManager, self).get_query_set()
        return queryset.filter(is_draft=False, pub_date__lte=datetime.now())

class Entry(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        unique_for_date='pub_date',
        help_text='Automatically built from the title.',
    )
    body_source = models.TextField('Body')
    body = models.TextField(
        'Body as HTML', 
        blank=True, 
        null=True,
        editable=False,
    )
    markup = models.CharField(
        'Markup language',
        default='markdown',
        max_length=8, 
        choices=MARKUP_CHOICES,
    )
    is_draft = models.BooleanField(
        'Draft',
        default=False,
        help_text='Draft entries is not published.',
    )
    pub_date = models.DateTimeField('Date published', default=datetime.now)

    # managers
    objects = models.Manager()
    published = PublishedEntriesManager()

    class Meta:
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return self.title

    def save(self):
        self.body = markuping(self.markup, self.body_source)
        super(Entry, self).save()    

    def get_absolute_url(self):
        return '/weblog/%s/%s/' % (self.pub_date.strftime('%Y/%m/%d').lower(), self.slug)


# signals

from django.db.models import signals

def entry_pre_save(sender, instance, signal, *args, **kwargs):
    # update pub_date instance if entry was draft
    try:
        e = Entry.objects.get(id=instance.id)
        if e.is_draft:
            instance.pub_date = datetime.now()
    except Entry.DoesNotExist:
        pass

signals.pre_save.connect(entry_pre_save, sender=Entry)
signals.post_save.connect(post_to_twitter, sender=Entry)
