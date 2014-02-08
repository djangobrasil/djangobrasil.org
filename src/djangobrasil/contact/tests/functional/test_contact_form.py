from django.core.exceptions import ValidationError
from django.forms.widgets import Textarea
from django.utils.unittest import TestCase

from djangobrasil.contact.forms import ContactForm


class ContactFormTestCase(TestCase):

    def test_should_have_a_name_field(self):
        self.assertIn('name', ContactForm.base_fields)

    def test_field_name_must_have_max_length_50(self):
        self.assertEqual(50, ContactForm.base_fields['name'].max_length)

    def test_should_have_a_from_email_field(self):
        self.assertIn('from_email', ContactForm.base_fields)

    def test_from_email_field_validator(self):
        self.assertRaises(
            ValidationError,
            ContactForm.base_fields['from_email'].run_validators,
            'email_invalido'
        )

    def test_should_have_a_subject_field(self):
        self.assertIn('subject', ContactForm.base_fields)

    def test_subject_field_must_have_max_length_100(self):
        self.assertEqual(100, ContactForm.base_fields['subject'].max_length)

    def test_should_have_a_message_field(self):
        self.assertIn('message', ContactForm.base_fields)

    def test_message_field_must_be_a_text_area(self):
        contact_form_widget = ContactForm.base_fields['message'].widget
        self.assertTrue(isinstance(contact_form_widget, Textarea),
                        "Message field's widget must be a Textarea instance, \
                        found a %s's instance" % contact_form_widget.__class__)
