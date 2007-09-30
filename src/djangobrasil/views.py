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


from django.contrib import databrowse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from djangobrasil.forms import ContactForm
from djangobrasil.settings import MANAGERS

def db(*args, **kwargs):
    return databrowse.site.root(*args, **kwargs)
db = login_required(db)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            from_email = '%s <%s>' % (request.POST.get('name', ''),
                                      request.POST.get('from_email', ''))
            try:
                send_mail(subject, message, from_email, MANAGERS,
                          fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contato/?enviado=ok')
    else:
        form = ContactForm()
    enviado = bool(request.GET.get('enviado', ''))
    return render_to_response('flatfiles/contato.html',
                              {'form': form, 'enviado': enviado})
