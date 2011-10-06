# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from djangobrasil.aggregator.forms import FeedForm


def participe_dos_feeds(request):
    enviado = 'False'
    if request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            subject = '[django-br] Nova participação nos Feeds'
            message = '%s <%s> solicitou sua adicao aos feeds da comunidade. Blog: %s' % (request.POST.get('title',''), request.POST.get('email',''), request.POST.get('public_url',''))
            from_email = '%s <%s>' % (request.POST.get('title', ''),
                                      request.POST.get('email', ''))
            recipient_list = [mail_tuple[1] for mail_tuple in settings.MANAGERS]
            try:
                send_mail(subject, message, from_email, recipient_list,
                          fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            form.save()
            del(form)
            form = FeedForm()
            enviado = 'ok'
    else:
        form = FeedForm()
        enviado = False
    return render_to_response('flatfiles/participe.html',
                              {'form': form, 'enviado': enviado,},
                              context_instance=RequestContext(request))
