from django.db import models
from MonumentType.models import MonumentType

class Monument(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    author = models.CharField(max_length=200)
    monument_type = models.ForeignKey(MonumentType, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='monuments/')
    description = models.TextField()

    def __str__(self):
        return self.name