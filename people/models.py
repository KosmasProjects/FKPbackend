from django.db import models
from organization.models import Organization


class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200)


# Create your models here.
