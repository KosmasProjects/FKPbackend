from django.db import models

class MonumentType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='monument_types/')

    def __str__(self):
        return self.name