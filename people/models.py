from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


# Create your models here.
