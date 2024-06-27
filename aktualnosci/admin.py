from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'author', 'created_at', 'updated_at', 'image', 'fundacja_kochania_poznania', 'pomniki_poznania', 'wspolna_sprawa', 'cieliczko_pl', 'poznanskie_legendy']

admin.site.register(Blog, BlogAdmin)