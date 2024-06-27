from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    author = models.CharField(max_length=200)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="blog_images/", null=True, blank=True)
    fundacja_kochania_poznania = models.BooleanField(default=False)
    pomniki_poznania = models.BooleanField(default=False)
    wspolna_sprawa = models.BooleanField(default=False)
    cieliczko_pl = models.BooleanField(default=False)
    poznanskie_legendy = models.BooleanField(default=False)
    # Add more BooleanField for other websites

    def __str__(self):
        return self.title