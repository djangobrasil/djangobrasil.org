from django import forms
from captcha.fields import CaptchaField
from models import SuccessCase


class NewCaseForm(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = SuccessCase
