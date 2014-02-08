from django.core import mail
from django.conf import settings
from django.contrib import messages
from django.views.generic import FormView

from contact.forms import ContactForm


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '/contato/'

    def form_valid(self, form, *args, **kwargs):
        from_email = '%s <%s>' % (form.data['name'], form.data['from_email'])
        recipients = [manager[1] for manager in settings.MANAGERS]

        try:
            mail.send_mail(
                form.data['subject'],
                form.data['message'],
                from_email,
                recipients
            )
            messages.success(self.request, 'Mensagem enviado com sucesso')
        except mail.BadHeaderError:
            messages.error(self.request, 'Invalid header found')
            return self.render_to_response(
                context=self.get_context_data(form=form))

        return super(self.__class__, self).form_valid(form)
