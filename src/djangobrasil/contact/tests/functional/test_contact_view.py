from django.utils.unittest import TestCase
from django.test import RequestFactory

from contact.views import ContactView
from contact.forms import ContactForm


class ContactViewTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('contact_view')

    def test_view_must_have_a_template_name(self):
        response = ContactView.as_view()(self.request)
        self.assertTrue(response.template_name)

    def test_view_must_have_success_url(self):
        pass

    def test_view_must_have_a_form_class(self):
        self.assertEquals(ContactForm, ContactView.form_class)

    def test_should_request_the_contacts_view_via_get_directly_and_be_success(self):
        response = ContactView.as_view()(self.request)
        self.assertEqual(response.status_code, 200)

    def test_should_request_the_contacts_view_via_post_directly_with_no_data_and_get_an_error(self):
        request = RequestFactory().post('contact_view')
        response = ContactView.as_view()(request)
        self.assertEqual(response.status_code, 200)
