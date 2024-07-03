
from django.db import models
from organization.models import Organization
from django.conf import settings

import os

class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200)
    photo_url = models.URLField(null=True, blank=True)
