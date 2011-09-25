from django.core import mail
from django.core.urlresolvers import reverse
from django.conf import settings
from django.test import RequestFactory, Client
from django.utils.unittest import TestCase

from contact.views import ContactView
from contact.forms import ContactForm


class SendMailMock(object):

    def send_mail_mock(self, subject, message, from_email, recipient_list):
        self.subject = subject
        self.message = message
        self.from_email = from_email
        self.recipient_list = recipient_list

class SendMailTestCase(TestCase):

    def setUp(self):
        self.send_mail = mail.send_mail


class ContactViewSendMailMock(TestCase):

    def setUp(self):
        self.send_mail = mail.send_mail
        self.send_mail_mock_obj = SendMailMock()
        mail.send_mail = self.send_mail_mock_obj.send_mail_mock

    def tearDown(self):
        mail.send_mail = self.send_mail


class ContactViewTestCase(ContactViewSendMailMock):

    def setUp(self):
        super(self.__class__, self).setUp()

        self.client = Client()
        self.post_data = {
            'name': 'eu',
            'from_email': 'foo_bar@gmail.com',
            'subject': 'foo',
            'message': 'bar'
        }

    def test_view_must_have_a_template_name(self):
        response = self.client.get(reverse('contact'))
        self.assertTrue(response.template_name)

    def test_view_must_have_success_url(self):
        self.assertEqual('/contato/', ContactView.success_url)

    def test_view_must_have_a_form_class(self):
        self.assertEqual(ContactView.form_class, ContactForm)

    def test_should_request_the_contacts_view_via_get_directly_and_be_success(self):
        response = self.client.get(reverse('contact'))
        self.assertSuccess(response.status_code)

    def test_should_post_to_the_view_and_get_a_redirect(self):
        response = self.client.post(reverse('contact'), self.post_data)
        self.assertEqual(302, response.status_code)

    def test_should_post_to_the_view_and_get_a_redirect_to_contato_url(self):
        response = self.client.post(reverse('contact'), self.post_data)
        self.assertIn('/contato/', response['Location'])

    def test_should_get_the_view_with_an_real_request_object_and_be_success(self):
        response = self.client.get(reverse('contact'))
        self.assertSuccess(response.status_code)

    def test_should_not_redirect_when_theres_no_message(self):
        del self.post_data['message']
        response = self.client.post(reverse('contact'), self.post_data)
        self.assertNotEqual(302, response.status_code)

    def test_should_not_redirect_when_email_is_in_an_invalid_format(self):
        self.post_data['from_email'] = 'foo'
        response = self.client.post(reverse('contact'), self.post_data)
        self.assertNotEqual(302, response.status_code)

    def assertSuccess(self, status_code):
        self.assertEqual(200, status_code, "Status code should be 200, got %s" % status_code)


class ContactViewSendMailTestCase(ContactViewSendMailMock):

    def setUp(self):
        super(self.__class__, self).setUp()

        self.post_data = {
            'name': 'eu',
            'from_email': 'foo_bar@gmail.com',
            'subject': 'foo',
            'message': 'bar'
        }

        self.client = Client()
        self.response = self.client.post(reverse('contact'), self.post_data)

    def test_should_call_send_mail_with_the_subject_sent_from_the_form(self):
        self.assertEqual(self.post_data['subject'], self.send_mail_mock_obj.subject)

    def test_should_call_send_mail_with_the_message_sent_from_the_form(self):
        self.assertEqual(self.post_data['message'], self.send_mail_mock_obj.message)

    def test_should_call_send_mail_with_formated_from_email(self):
        expected_format = '%s <%s>' % (self.post_data['name'], self.post_data['from_email'])
        self.assertEqual(expected_format, self.send_mail_mock_obj.from_email)

    def test_should_call_send_mail_with_correct_recipient_list(self):
        recipient_list = [manager[1] for manager in settings.MANAGERS]
        self.assertEqual(recipient_list, self.send_mail_mock_obj.recipient_list)

    def test_should_post_with_valid_data_and_get_a_success_message(self):
        self.assertIn('Mensagem enviado com sucesso', self.response.cookies.values()[0].value)


class ContactViewSendMailExceptionTestCase(TestCase):

    def setUp(self):
        class SendMailMock(object):

            def send_mail_mock(self, subject, message, from_email, recipient_list):
                raise mail.BadHeaderError

        self.send_mail = mail.send_mail
        mail.send_mail = SendMailMock().send_mail_mock

        self.post_data = {
            'name': 'eu',
            'from_email': 'foo_bar@gmail.com',
            'subject': 'foo',
            'message': 'bar'
        }

        client = Client()
        self.response = client.post(reverse('contact'), self.post_data)

    def tearDown(self):
        mail.send_mail = self.send_mail

    def test_shold_catch_bad_header_error_exception_and_show_a_message_in_rendered_content(self):
        self.assertIn('Invalid header found', self.response.rendered_content)
