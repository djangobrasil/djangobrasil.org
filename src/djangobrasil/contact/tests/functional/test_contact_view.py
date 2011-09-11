from django.core.urlresolvers import reverse
from django.test import RequestFactory, Client
from django.utils.unittest import TestCase

from contact.views import ContactView
from contact.forms import ContactForm


class ContactViewTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('contact_view')
        self.client = Client()

    def test_view_must_have_a_template_name(self):
        response = ContactView.as_view()(self.request)
        self.assertTrue(response.template_name)

    def test_view_must_have_success_url(self):
        self.assertEqual('contato/', ContactView.success_url)

    def test_view_must_have_a_form_class(self):
        self.assertEqual(ContactForm, ContactView.form_class)

    def test_should_request_the_contacts_view_via_get_directly_and_be_success(self):
        response = ContactView.as_view()(self.request)
        self.assertSuccess(response.status_code)

    def test_should_post_to_the_view_and_get_a_redirect(self):
        request = RequestFactory().post('contact_view')
        response = ContactView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_should_post_to_the_view_and_get_a_redirect_to_url_contato(self):
        request = RequestFactory().post('contact_view')
        response = ContactView.as_view()(request)
        self.assertEqual(response['Location'], 'contato/')

    def test_should_get_the_view_with_an_real_request_object_and_be_success(self):
        response = self.client.get(reverse('contact'))
        self.assertSuccess(response.status_code)

    def assertSuccess(self, status_code):
        self.assertEqual(status_code, 200, "Status code should be 200, got %s" % status_code)
