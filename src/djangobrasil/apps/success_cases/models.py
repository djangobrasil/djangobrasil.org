# coding: utf-8

from django.db import models
from django.template.defaultfilters import slugify


class SuccessCase(models.Model):

    title = models.CharField(max_length=100, verbose_name="Título")
    short_description = models.CharField(
        max_length=250, verbose_name="Descrição resumida"
    )
    long_description = models.TextField(verbose_name="Descrição Completa")
    author = models.CharField(max_length=200, verbose_name="Autor")
    email = models.EmailField(max_length=100, verbose_name="Email")
    url = models.URLField(max_length=10000)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SuccessCase, self).save(*args, **kwargs)
