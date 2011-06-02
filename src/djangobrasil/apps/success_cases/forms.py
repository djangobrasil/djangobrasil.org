from django import forms
from models import SuccessCase
from recaptcha_works.fields import RecaptchaField


class NewCaseForm(forms.ModelForm):

    recaptcha = RecaptchaField(label='Captcha', required=True)

    class Meta:
        model = SuccessCase
        exclude = ('slug',)
