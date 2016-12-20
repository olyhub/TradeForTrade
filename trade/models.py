from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):

    class Meta:
        app_label = "trade"

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=20)
    trade = models.CharField(max_length=300)
    location = models.CharField(max_length=300)