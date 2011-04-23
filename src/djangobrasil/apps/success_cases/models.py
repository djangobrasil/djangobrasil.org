from django.db import models


class SuccessCase(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    url = models.URLField(max_length=10000)
