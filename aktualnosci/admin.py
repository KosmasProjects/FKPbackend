from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title', 'author__username']
    list_filter = ['created_at']

admin.site.register(Blog, BlogAdmin)