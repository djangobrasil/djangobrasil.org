from django import forms
from models import SuccessCase


class NewCaseForm(forms.ModelForm):

    class Meta:
        model = SuccessCase
            
#    title = forms.CharField(max_length=200, required=True)
#    description = forms.CharField(required=True, widget=forms.Textarea())
#    author = forms.CharField(max_length=200, required=True)
#    email = forms.EmailField(max_length=100, required=True)
#    url = forms.URLField(max_length=10000, required=True)
