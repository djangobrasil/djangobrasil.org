from django.views.generic import FormView

from contact.forms import ContactForm


class ContactView(FormView):
    template_name = 'flatfiles/contato.html'
    form_class = ContactForm
    success_url = 'contato/'
