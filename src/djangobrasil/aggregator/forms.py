# -*- coding: utf-8 -*-
from django import forms
from djangobrasil.aggregator.models import Feed

class FeedForm(forms.ModelForm):
    title = forms.CharField(label="Título", max_length=50)
    email = forms.EmailField(label="E-mail")
    feed_url = forms.URLField(label="URL Feed", verify_exists=False)
    public_url = forms.URLField(label="URL Pública",verify_exists=False)

    class Meta:
        model = Feed
