# -*- coding: utf-8 -*-
#
#  Copyright (c) 2005, the Lawrence Journal-World
#  All rights reserved.
#
#  See LICENSE file in src/djangobrasil/apps/aggregator/ directory.
#

from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from djangobrasil.aggregator.models import Feed
from django.core.mail import send_mail
from djangobrasil import settings
from django.http import BadHeaderError, HttpResponseRedirect

class FeedAdmin(ModelAdmin):
    list_display = ("title", "public_url", "is_defunct","accepted","email_sent")
    list_filter = ("is_defunct","accepted","email_sent")
    ordering = ("title",)
    search_fields = ("title", "public_url")
    list_per_page = 500
    exclude = ['email_sent']

    def save_model(self, request, obj, form, change):
        if obj.accepted and not obj.email_sent:
            subject = "[django-br] Sua participação foi aceita!"
            message = "Prezado, sua solicitacao (%s) foi aceita, seus feeds serao adicionados em breve." % obj.public_url
            from_email = '%s <%s>' % (obj.title,
                                      obj.email)
            recipient_list = [mail_tuple[1] for mail_tuple in settings.MANAGERS]
            recipient_list.append(obj.email)
            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                obj.email_sent=True
                obj.save()
            except BadHeaderError:
                msg = 'Ocorreu um erro ao enviar o e-mail.'
                self.message_user(request, msg)
                post_url = '../'
                return HttpResponseRedirect(post_url)
        obj.save()

admin.site.register(Feed, FeedAdmin)
