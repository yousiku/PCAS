from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Keywords(models.Model):
    skuid = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    keywords = models.CharField(max_length=200)