from django.db import models
from django.template.defaultfilters import slugify


class SuccessCase(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    url = models.URLField(max_length=10000)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SuccessCase, self).save(*args, **kwargs)
